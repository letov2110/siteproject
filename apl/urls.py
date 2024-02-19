from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("post1/", views.post1, name="post1"),
    path("post2/", views.post2, name="post2"),
    path("", views.index, name="index"),
    path('aaa/', views.aaa, name='aaa'),
   
]
