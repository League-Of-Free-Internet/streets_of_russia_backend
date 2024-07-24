from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="empty_project",
        default_version='v1',
        description="Документация для приложений проекта empty_project",
        contact=openapi.Contact(email="admin@empty_project.ru"),
        license=openapi.License(name="MIT license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("empty_project_backend/admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    )
]

handler400 = "core.utils.bad_request"
handler403 = "core.utils.forbidden"
handler404 = "core.utils.not_found"
handler500 = "core.utils.server_error"
