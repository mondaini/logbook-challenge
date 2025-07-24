from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from pilotlog.views import (
    LogbookViewSet,
)

router = DefaultRouter()
router.register(r"logbook", LogbookViewSet, basename="logbook")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
