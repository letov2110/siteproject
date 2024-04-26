from django.urls import path
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
    path("base/", views.base, name="base"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),   
    path("create/", views.create, name="create"),
    path('show/', views.show, name='show'),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('api/command', views.PostListApiView.as_view(),name='post-api'),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
