from django.forms import ModelForm, CharField,TextInput,PasswordInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import  MyUser


class UserReg(ModelForm):
    password = CharField(widget=forms.PasswordInput())
    class Meta:
        model = MyUser
        fields = ['username', 'password','email']

class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())


class EditUser(ModelForm):
    class Meta:
        model = MyUser
        fields = ['nickname', 'email','first_name','last_name','birsday' ,'about', 'ava']
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'nickname': forms.TextInput(attrs={'required': True}),
        }
