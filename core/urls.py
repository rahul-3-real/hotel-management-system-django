from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls", namespace="base")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
]


# Serving static files in development.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving media files in development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
