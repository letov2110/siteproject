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
    path('show/', views.show, name='show'),
    path("show/edit/<int:id>/", views.edit),
    path("show/delete/<int:id>/", views.delete),
    path('edit_good/', views.edit_good, name='edit_good'),
    #later del

path('forum/', views.forum, name='forum'),
    #later del

    
#later del
path('show1/', views.PostPostListCreate.as_view(),name='post-view-create'),
path('show2/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view(),name='retrieve-update-destroy')
#later del
#######
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)