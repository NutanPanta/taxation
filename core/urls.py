from django.urls import re_path, include, path
from django.conf import settings
from django.conf.urls.static import static
from v1.admin import admin_site as project_admin

urlpatterns = [
    path("management/", project_admin.urls),
    re_path(r"^v1/", include(("v1.urls", "v1"), namespace="v1")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
