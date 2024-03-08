from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    about = models.TextField(blank=True)
    ava = models.ImageField(upload_to='static/images/reglog',blank=True)
    
    

    def __str__(self):
        return self.nickname
