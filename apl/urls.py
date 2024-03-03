from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),   
    ###
    path("create/", views.create, name="create"),
    path("create_good/", views.create_good, name="create_good"),    
    ########
    path('register/',views.register, name='register'),
    path('register_good/',views.register_good, name='register_good'),
    ###########
    path("login/", views.login_page, name="login"),
    path("log_in_good/", views.log_in_good, name="log_in_good"),
    path("logout/", views.logout_page),
    ###########
    path('show/', views.show, name='show'),
    path("show/edit/<int:id>/", views.edit),
    path("show/delete/<int:id>/", views.delete),
    path('edit_good/', views.edit_good, name='edit_good'),
    #potom del
path('artic/', views.artic, name='artic'),
path('forum/', views.forum, name='forum'),
    #potom del
#######
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)