from rest_framework import permissions, viewsets

from api.pagination import EventsPagination, NewsPagination
from api.serializers import EventsSerializer, NewsSerializer, UserSerializer
from api.serializers import DisciplinesSerializer
from events.models import Events
from news.models import News
from disciplines.models import Disciplines
from users.models import CustomUser


class NewsViewSet(viewsets.ModelViewSet):
    """
    Реализует операции с моделью News:
    - получения списка новостей;
    - создание новой новости;
    - редактирование новости;
    - удаление новости.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
    http_method_names = ("get", "post", "patch", "delete")
    search_fields = ("name",)
    lookup_field = "name"


class UserViewSet(viewsets.ModelViewSet):
    """
    Работа с пользователями. Только для администратора.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    lookup_field = "email"
    search_fields = ("email", "phone_number", "first_name", "last_name")
    http_method_names = ("post",)


class EventsViewSet(viewsets.ModelViewSet):
    """
    Работа с событиями. Только для администратора.
    """

    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    pagination_class = EventsPagination
    # permission_classes = (permissions.IsAuthenticated,
    #                       permissions.IsAdminUser)
    lookup_field = "email"
    search_fields = (
        "name", "start_date", "place", "deadline_registration_date"
    )
    http_method_names = ("get", "post", "patch", "delete")


class DisciplinesViewSet(viewsets.ModelViewSet):
    """
    Работа с событиями. Только для администратора.
    """

    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesSerializer
    lookup_field = "email"
    search_fields = ("name",)
    http_method_names = ("get",)
