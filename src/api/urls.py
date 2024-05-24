from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet, UserViewSet

router_v1 = DefaultRouter()

router_v1.register(
    r"news",
    NewsViewSet,
    basename="news"
)
router_v1.register(r"users",
                   UserViewSet,
                   basename="users")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
