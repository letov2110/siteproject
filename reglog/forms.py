from django.contrib.auth.models import User
from django.forms import ModelForm, CharField,TextInput,PasswordInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import  MyUser


class UserReg(ModelForm):
    password = CharField(widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ['username', 'password']

class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())

from django import forms
# from .models import User

class EditUser(ModelForm):
    class Meta:
        model = MyUser
        fields = ['nickname', 'email', 'about', 'ava']

