from django.db import models
from django.contrib.auth.models import User

class Cat_topics(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Forum_Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    cat_topic = models.ManyToManyField(Cat_topics ,blank=False)
    def __str__(self):
        return self.title
    


class Forum_Answer(models.Model):
    post = models.ForeignKey(Forum_Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=0)
    def __str__(self): 
        return self.text
    
class VotedComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Forum_Answer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'answer')
