from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('tabla.urls')),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ##urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)