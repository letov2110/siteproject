from django.contrib.auth.models import User
from django.forms import ModelForm, CharField,TextInput,PasswordInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Post


class UserReg(ModelForm):
    password = CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())

class AddPost(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title',  'content','categories' ]

