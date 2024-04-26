
from .models import Tutor, Comm_tut
from django import forms

class CommForm(forms.ModelForm):
    class Meta:
        model = Comm_tut
        fields = [ 'text']

class TutorForm(forms.ModelForm):
    
    class Meta:
        model = Tutor
        fields = ['title', 'public_text']
        