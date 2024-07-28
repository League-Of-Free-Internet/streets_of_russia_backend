from django.urls import include, path

from api.routers import CustomRouter
from api.views import (
    DisciplinesFullViewSet,
    DisciplinesNamesListViewSet,
    DisciplinesShortViewSet,
    DisciplinesViewSet,
    EventSignOutViewSet,
    EventSignUpViewSet,
    EventViewSet,
    FourLatestEventsViewSet,
    NewsViewSet,
    ProjectTokenObtainPairView,
    ProjectTokenRefreshView,
    UserViewSet,
)

router_v1 = CustomRouter()

router_v1.register(
    r"events", FourLatestEventsViewSet, basename="latest-events"
)
router_v1.register(
    r"event", EventViewSet, basename="event"
)
router_v1.register(
    r"event/(?P<event_id>\d+)/sign-up",
    EventSignUpViewSet,
    basename="event-sign-up"
)
router_v1.register(
    r"event/(?P<event_id>\d+)/sign-out",
    EventSignOutViewSet,
    basename="event-sign-out"
)
router_v1.register(r"news", NewsViewSet, basename="news")
router_v1.register(r"users", UserViewSet, basename="users")
router_v1.register(r"disciplines", DisciplinesViewSet,
                   basename="disciplines")
router_v1.register(
    r"disciplines-names", DisciplinesNamesListViewSet,
    basename="disciplines-names"
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
    path("token/", ProjectTokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("token/refresh/", ProjectTokenRefreshView.as_view(),
         name="token_refresh"),
]

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/auth/", include(registration_uls))
]
