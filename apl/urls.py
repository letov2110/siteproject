from django.urls import path
from . import views
urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),   
    path("create/", views.create, name="create"),
    path("create_good/", views.create_good, name="create_good"),    
    ########
    path('register/',views.register, name='register'),
    path('register_good/',views.register_good, name='register_good'),
    ###########
    path("login/", views.login_page, name="login"),
    path("log_in_good/", views.log_in_good, name="log_in_good"),

    ###########
    path('show/', views.show, name='show'),
    path("show/edit/<int:id>/", views.edit),
    path("show/delete/<int:id>/", views.delete),
    path('show/edit/<int:id>/edit_good/', views.edit_good, name='edit_good'),
#######
    
    ]