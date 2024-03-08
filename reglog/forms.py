from django.contrib.auth.models import User
from django.forms import ModelForm, CharField,TextInput,PasswordInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserReg(ModelForm):
    password = CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','email', 'password']

class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())

from django import forms
from .models import User

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'about', 'ava']

