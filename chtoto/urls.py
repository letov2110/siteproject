
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from filebrowser.sites import site

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apl.urls")),
    path("newart/", include("newart.urls")),
    path("reglog/", include("reglog.urls")),
    path('tinymce/', include('tinymce.urls')),    
    path("__debug__/", include(debug_toolbar.urls)),
    path('tutor/', include('tutor.urls')),

    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),


   

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
