from django.urls import path
from . import views
urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),   
    path("create/", views.create, name="create"),
    path("create_good/", views.create_good, name="create_good"),    
    path('register/',views.register, name='register'),
    path('register_good/',views.register_good, name='register_good'),
    ###########
    path("login/", views.login, name="login"),
    ###########
    path('show/', views.show, name='show'),
]