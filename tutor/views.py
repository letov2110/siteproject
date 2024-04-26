from django.shortcuts import render
from .models import Tutor, Comm_tut
from .forms import CommForm,TutorForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def showtutor(request):
    all_tut = Tutor.objects.all()
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
