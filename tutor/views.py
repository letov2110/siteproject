from django.shortcuts import render, redirect
from .models import Tutor, Comm_tut
from .forms import CommForm,TutorForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def showtutor(request):
    all_tut = Tutor.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        all_tut = all_tut.filter(title__icontains=search_query)
    return render(request, 'tutor/showtutor.html', {'all_tut': all_tut})
    
def d_tutor(request, post_id):
    post = Tutor.objects.get(id=post_id)
    post.views += 1
    post.save()
    comments = Comm_tut.objects.filter(post=post_id).order_by('-pub_date')
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
    return render(request, 'tutor/d_tutor.html', {'post': post, 'comments': comments, 'form': form})

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

def delete_comment(request, post_id, comment_id):
    post = Tutor.objects.get(id=post_id)
    comment = Comm_tut.objects.get(id=comment_id)
    if request.user == comment.author:
        comment.delete()
        return redirect('d_tutor', post_id=post_id)
    else:
        return HttpResponseForbidden()