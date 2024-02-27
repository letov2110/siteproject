from django.db import models
from django.utils.text import slugify
from django.forms import ModelForm
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)    
    content = models.TextField()
    categories = models.ManyToManyField(Category,blank=False)

    def __str__(self):
        return slugify(self.title)
    

