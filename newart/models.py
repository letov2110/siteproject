from django.db import models
from tinymce import models as tinymce_models

class Cat_News(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)  
    image = models.ImageField(upload_to='static/images/newart', blank=True)
    text = tinymce_models.HTMLField()
    date = models.DateTimeField()
    category = models.ManyToManyField(Cat_News)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title