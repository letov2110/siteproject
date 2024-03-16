from django.shortcuts import render
from .models import Tutor, Comm_tut
from .forms import CommForm,TutorForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,HttpResponse

def showtutor(request):
    all_tut = Tutor.objects.all()
    return render(request, 'tutor/showtutor.html', {'all_tut': all_tut})
    
def d_tutor(request, post_id):
    post = Tutor.objects.get(id=post_id)
    comments = Comm_tut.objects.filter(post=post_id)
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



from .task import my_task
def test_cel(request):
    my_task.delay()
    return HttpResponse("Started!")
from django_celery_beat.models import PeriodicTask, IntervalSchedule

def schedule_task(request):
    interval, err = IntervalSchedule.objects.get_or_create(
        every=30, period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.create(
        interval=interval,
        name="bubu-schedule",
        task="tutor.task.my_task",
        # args=json.dump(["arg1", True]),
        # on_off=True,
    )
    return HttpResponse("Scheduled!")