
from .models import Comm_tut
from django import forms
from tinymce.widgets import TinyMCE

class CommForm(forms.ModelForm):
    class Meta:
        model = Comm_tut
        fields = [ 'text']



class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
