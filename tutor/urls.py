from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.showtutor, name='showtutor'),
    path('post/<int:post_id>/', views.d_tutor, name='d_tutor'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path("tinymce/", include("tinymce.urls")),
]