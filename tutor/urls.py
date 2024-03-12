from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.showtutor, name='showtutor'),
    path('post/<int:post_id>/', views.d_tutor, name='d_tutor'),
    path('add_tutor/', views.add_tutor, name='add_tutor'),
    path("tinymce/", include("tinymce.urls")),
]