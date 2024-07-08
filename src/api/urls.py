from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (DisciplinesShortViewSet, DisciplinesViewSet, EventsViewSet,
                    NewsViewSet, UserViewSet)

router_v1 = DefaultRouter()

router_v1.register(r"events", EventsViewSet, basename="users")
router_v1.register(r"news", NewsViewSet, basename="news")
router_v1.register(r"users", UserViewSet, basename="events")
router_v1.register(
    r"disciplines", DisciplinesViewSet, basename="disciplines"
)
router_v1.register(
    r"discipline", DisciplinesShortViewSet,
    basename="disciplines-short"
)

registration_uls = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/auth/", include(registration_uls))
]
