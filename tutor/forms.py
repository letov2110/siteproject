
from .models import Comm_tut,Tutor
from django import forms
from tinymce.widgets import TinyMCE

class CommForm(forms.ModelForm):
    class Meta:
        model = Comm_tut
        fields = [ 'text']

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
    
class TutorForm(forms.ModelForm):
    # text = forms.CharField(widget=TinyMCEWidget(attrs={'required':False}))
    class Meta:
        model=Tutor
        fields =['image','title','text',]
