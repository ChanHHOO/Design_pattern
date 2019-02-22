from django.conf import settings
from django.conf.urls import (
    url, include
)
from django.conf.urls.static import static
from django.contrib import admin
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

urlpatterns = [
    # Django admin
    url(r'^sysadmin/',
        admin.site.urls),

    # Django-allauth
    url(r'^accounts/',
        include('allauth.urls')),

    # Wagtail
    url(r'^admin/',
        include(wagtailadmin_urls)),
    url(r'^documents/',
        include(wagtaildocs_urls)),
    url(r'',
        include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
