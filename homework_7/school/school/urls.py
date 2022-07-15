from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

DEBUG = True

urlpatterns = [
    path("", include("lessons.urls")),
    path("users/", include("users.urls")),
    path("products/", include("products.urls")),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
