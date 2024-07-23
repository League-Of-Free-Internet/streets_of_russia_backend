from rest_framework.routers import SimpleRouter

from api.views import EventSignOutViewSet


class CustomRouter(SimpleRouter):
    def get_lookup_regex(self, viewset, lookup_prefix=""):
        if viewset == EventSignOutViewSet:
            self.trailing_slash = ""
            return ""
        return super().get_lookup_regex(viewset, lookup_prefix)
