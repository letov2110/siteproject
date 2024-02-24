from django.urls import path,include
from . import views
urlpatterns = [
    path("home/", views.home, name="home"),
    # path("create/", views.create, name="create"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
    path("", views.base, name="base"),
    path('register/',views.register, name='register'),
    path('register_good/',views.register_good, name='register_good'),
   
]