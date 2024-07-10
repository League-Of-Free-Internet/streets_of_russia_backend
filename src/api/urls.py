from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import (DisciplinesFullViewSet, DisciplinesShortViewSet,
                       DisciplinesViewSet, EventSignUpViewSet, EventViewSet,
                       FourLatestEventsViewSet, NewsViewSet, UserViewSet)

router_v1 = DefaultRouter()

router_v1.register(
    r"events", FourLatestEventsViewSet, basename="latest-events"
)
router_v1.register(
    r"event", EventViewSet, basename="event"
)
router_v1.register(
    r'event/(?P<event_id>\d+)/sign-up', EventSignUpViewSet,
    basename='event-signup'
)
router_v1.register(r"news", NewsViewSet, basename="news")
router_v1.register(r"users", UserViewSet, basename="users")
router_v1.register(
    r"disciplines", DisciplinesViewSet, basename="disciplines"
)
router_v1.register(
    r"discipline", DisciplinesShortViewSet,
    basename="discipline-short"
)
router_v1.register(
    r"full-discipline", DisciplinesFullViewSet,
    basename="discipline-full"
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
