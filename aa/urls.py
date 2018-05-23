
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/counryVisa/visa/country/', include('counryVisa.urls')),
    path('admin/counryVisa/country/country/', include('counryVisa.urls')),
    path('admin/visa/vises/parse/', include('visa.urls')),
    path('admin/visa/vises/json/', include('visa.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('loginsys.urls')),
    path('my/', include('profiles.urls')),
    path('visa/', include('visa.urls')),
    path('doc/form/', include('dokument.urls')),
    path('doc/', include('Tour.urls')),
    path('about/', include('Tour.urls')),
    path('', include('Tour.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
