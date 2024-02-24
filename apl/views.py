from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from .models import Post

from .forms import UserReg


def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        user_form = UserReg(request.POST)
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
            
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            return redirect('register_good')
    else:
        user_form = UserReg()
    return render(request, 'register.html', {'user_form': user_form})

def register_good(request):
      return render(request,'register_good.html')


def index(request):
    fullteg=Post.object.all()
    return render(request, 'index.html',{'fullteg':fullteg})

def create(request):
    if request.method == "POST":
        teg = Post()
        teg.title = request.POST.get("title")
        teg.content = request.POST.get("content")
        teg.categories=request.POST.get('categories')
        teg.save()
    return HttpResponseRedirect("/")

