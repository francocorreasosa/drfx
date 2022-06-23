from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
