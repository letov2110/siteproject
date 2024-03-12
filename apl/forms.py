# from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from .models import Post

class AddPost(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title',  'content','categories' ]

