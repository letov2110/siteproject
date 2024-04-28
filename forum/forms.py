from django import forms
from .models import Forum_Question, Forum_Answer

class QuestionForm(forms.ModelForm):
    new_category = forms.CharField(label='New Category', required=False)
    class Meta:
        model = Forum_Question
        fields = ['title', 'text','cat_topic']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Forum_Answer
        fields = ['text']
