from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.showtutor, name='showtutor'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('post/<int:post_id>/', views.d_tutor, name='d_tutor'),
    path('add_tutor/', views.add_tutor, name='add_tutor'),
]