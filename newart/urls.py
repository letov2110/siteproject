from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
schema_view = get_schema_view(
    openapi.Info(
        title="My API", default_version="1.0.0", description="Documentation for my API"
    ),
    public=True,
)

urlpatterns = [
    path("shownews/", views.shownews, name="shownews"),
    path('shownews/<int:pk>',views.NewsView.as_view(),name='d_news'),
    path('api/news/', views.NewsListAPIView.as_view(), name='news-api'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)