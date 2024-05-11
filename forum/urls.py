from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_topics, name='all_topics'),
    path('add_topic/', views.add_topic, name='add_topic' ),
    path('top_question/<int:post_id>/', views.topic, name='topic'),
    path('edit_answer/<int:post_id>/<int:answer_id>/', views.edit_answer, name='edit_answer'),
    path('delete_answer/<int:post_id>/<int:answer_id>/', views.delete_answer, name='delete_answer'),
]