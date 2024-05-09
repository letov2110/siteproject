from django.db import models
from django.contrib.auth.models import User
from datetime import date
from forum.models import Forum_Answer
from django.db.models import Sum
from tutor.models import Tutor

class MyUser(User):
    nickname = models.CharField(max_length=50,blank=True)    
    about = models.TextField(blank=True)
    ava = models.ImageField(upload_to='static/images/reglog',blank=True)
    birsday=models.DateField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def calculate_age(self):
        if self.birsday:
            today = date.today()
            age = today.year - self.birsday.year - ((today.month, today.day) < (self.birsday.month, self.birsday.day))
            return age
        else:
            return None
    def total_rating(self):
        forum_rating = Forum_Answer.objects.filter(author=self).aggregate(Sum('rating'))['rating__sum']
        tutor_rating = Tutor.objects.filter(author=self).count() * 5
        
        total_rating = (forum_rating if forum_rating else 0) + tutor_rating
        
        return total_rating