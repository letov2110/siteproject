from django.contrib.auth.models import User
from django.forms import ModelForm, CharField
from django import forms
from .models import Post


class UserReg(ModelForm):
    password = CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

class LoginUser(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
    

class AddPost(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title',  'content','categories' ]



    
 
