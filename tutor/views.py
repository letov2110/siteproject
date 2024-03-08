from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Tutor, Comm_tut
from .forms import CommForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def showtutor(request):
    all_tut = Tutor.objects.all()
    return render(request, 'tutor/showtutor.html', {'all_tut': all_tut})

    
def d_tutor(request, post_id):
    tut = get_object_or_404(Tutor, id=post_id)
    
    tut.views += 1
    tut.save()
    comments = Comm_tut.objects.filter(post_id=post_id)
    addform = CommForm()
    return render(request, 'tutor/d_tutor.html', {'tut': tut, 'comments': comments, 'addform': addform})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Tutor, id=post_id)
    if request.method == 'POST':
        addform = CommForm(request.POST)
        if addform.is_valid():
            comment = addform.save()
            comment.post = post
            comment.author = request.user
            comment.save()
            # return redirect('d_tutor', post_id=post.id)
        return redirect('d_tutor', post_id=post.id)
    else:
        addform = CommForm()
    
    return render(request, 'add_comment.html', {'addform': addform})
