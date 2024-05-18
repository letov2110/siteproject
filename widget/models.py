from django.db import models
from tinymce import models as tinymce_models
from django.conf import settings


class QuestionType(models.TextChoices):
    SINGLE = 'single', 'Single choice'
    MULTIPLE = 'multiple', 'Multiple choice'

class Question(models.Model):
    name = models.CharField(max_length=50)
    q_text=tinymce_models.HTMLField()
    question_type = models.CharField(max_length=255,choices=QuestionType.choices,default=QuestionType.SINGLE,)
    cost_rating = models.IntegerField(default=2)
    def __str__(self) -> str:
        return f"{self.name}"
    def get_answers(self) -> list:
        return self.answer_set.filter(is_correct=True).values_list('name', flat=True) if self.question_type == QuestionType.MULTIPLE else [self.answer_set.filter(is_correct=True).first().name]

class Answer(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_set')
    name = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.question.name})"
    
class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    class Meta:
        unique_together = ('user', 'question')