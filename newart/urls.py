from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("shownews/", views.shownews, name="shownews"),
    path('shownews/<int:pk>',views.NewsView.as_view(),name='d_news'),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)