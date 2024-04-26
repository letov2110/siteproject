from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Tutor(models.Model):
    title = models.CharField(max_length=100)
    text = CKEditor5Field('text', config_name='default')
    public_text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Comm_tut(models.Model):
    post = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self): 
        return self.text