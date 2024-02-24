from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    subtitle = models.CharField(max_length=20,blank=True)
    content = models.CharField(max_length=250,blank=False)
    page = models.IntegerChoices("Pages", "1 2 3")
    categories = models.ManyToManyField(Category,blank=False)

    def __str__(self):
        return slugify(self.title)
