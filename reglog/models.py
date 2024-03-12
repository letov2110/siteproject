from django.db import models
from django.contrib.auth.models import User
class MyUser(User):
    nickname = models.CharField(max_length=50,blank=True)    
    about = models.TextField(blank=True)
    ava = models.ImageField(upload_to='static/images/reglog',blank=True)
    
    

