from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path("", include("apl.urls")),
    
    path("reglog/", include("reglog.urls")),
    path("newart/", include("newart.urls")),
    path("tutor/", include("tutor.urls")),
    path("forum/", include("forum.urls")),
    path("widget/", include("widget.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
