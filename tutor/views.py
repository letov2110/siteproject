from django.shortcuts import render, redirect
from .models import Tutor, Comm_tut
from .forms import CommForm,TutorForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator

def showtutor(request):
    all_tut = Tutor.objects.all()
    search_query = request.GET.get('search')
    paginator = Paginator(all_tut, 5)
    page_number = request.GET.get('page')
    if page_number and page_number.isdigit():
        page_number = int(page_number)
        page_obj = paginator.page(page_number)
    else:
        page_obj = paginator.page(1)
    if search_query:
        all_tut = Tutor.objects.filter(title__icontains=search_query)
    else:
        all_tut = page_obj.object_list
    return render(request, 'tutor/showtutor.html', {'all_tut': all_tut, 'page_obj': page_obj})    

def d_tutor(request, post_id):
    post = Tutor.objects.get(id=post_id)
    post.views += 1
    post.save()
    comment_list = Comm_tut.objects.filter(post=post).order_by('-pub_date')
    list = Comm_tut.objects.all()
    paginator = Paginator(list, 5)
    page_number = request.GET.get('page')
    if page_number and page_number.isdigit():
        page_number = int(page_number)
        page_obj = paginator.page(page_number)
    else:
        page_obj = paginator.page(1)
    if request.method == 'POST':
        form = CommForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('d_tutor', post_id=post_id)
    else:
        form = CommForm()
    return render(request, 'tutor/d_tutor.html', {'post': post, 'page_obj': page_obj, 'post_id': post_id, 'form': form, 'comment_list': comment_list})

@login_required(login_url='login')
def add_tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.author=request.user
            tutor.save()
            return redirect('showtutor')
    else:
        form = TutorForm()
    return render(request, 'tutor/add_tutor.html', {'form': form})

@login_required(login_url='login')
def edit_comment(request, post_id, comment_id):
    post = Tutor.objects.get(id=post_id)
    comment = Comm_tut.objects.get(id=comment_id)
    if request.method == 'POST':
        form = CommForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('d_tutor', post_id=post_id)
    else:
        form = CommForm(instance=comment)
    return render(request, 'tutor/d_tutor.html', {'post': post, 'comment': comment, 'form': form})

@login_required(login_url='login')
def delete_comment(request, post_id, comment_id):
    post = Tutor.objects.get(id=post_id)
    comment = Comm_tut.objects.get(id=comment_id)
    if request.user == comment.author:
        comment.delete()
        return redirect('d_tutor', post_id=post_id)
    else:
        return HttpResponseForbidden()