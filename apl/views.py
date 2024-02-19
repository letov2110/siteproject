from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, "home.html" )


def post1(request):
    post = Post.objects.get(id=1)
    return render(request, "post1.html", {'post1': post})


def post2(request):
    post = Post.objects.get(id=3)
    return render(request, "post2.html", {'post2': post})


def index(request):
    return render(request, "index.html")

def aaa(request):
    return render(request,'aaa.html')
