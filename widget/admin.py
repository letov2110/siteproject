from django.contrib import admin
from widget.models import *

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)
