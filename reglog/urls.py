from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
   
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('user_list/', views.user_list, name='user_list'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)