from rest_framework import permissions, response, viewsets

from api.pagination import EventsPagination, NewsPagination
from api.serializers import (DisciplinesNamesListSerializer, EventsSerializer,
                             NewsSerializer, UserSerializer)
from disciplines.models import Disciplines
from events.models import Events
from news.models import News
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
    lookup_field = "id"


class UserViewSet(viewsets.ModelViewSet):
    """
    Работа с пользователями.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ("post",)


class EventsViewSet(viewsets.ModelViewSet):
    """
    Работа с событиями. Только для администратора.
    """

    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    pagination_class = EventsPagination
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    search_fields = (
        "name", "start_date", "place", "deadline_registration_date"
    )
    http_method_names = ("get", "post")
    lookup_field = "id"


class DisciplinesViewSet(viewsets.ViewSet):
    """
    Работа со спортивными дисциплинами.
    """

    def list(self, request):
        disciplines = Disciplines.objects.all()
        names = [discipline.name for discipline in disciplines]
        serializer = DisciplinesNamesListSerializer(
            data={"names": names}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data)
