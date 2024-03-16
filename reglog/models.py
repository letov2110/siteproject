from django.db import models
from django.contrib.auth.models import User
from datetime import date
class MyUser(User):
    nickname = models.CharField(max_length=50,blank=True)    
    about = models.TextField(blank=True)
    ava = models.ImageField(upload_to='static/images/reglog',blank=True)
    birsday=models.DateField(blank=True, null=True)
    def calculate_age(self):
        if self.birsday:
            today = date.today()
            age = today.year - self.birsday.year - ((today.month, today.day) < (self.birsday.month, self.birsday.day))
            return age
        else:
            return None
        
    
    

