from django.urls import path
from . import views


from django.urls import path
from . import views

urlpatterns = [
    path('question_list', views.question_list, name='question_list'),
    path('<pk>', views.answer_question, name='answer_question'),

    
]
