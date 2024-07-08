from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from api.pagination import EventsPagination, NewsPagination
from api.serializers import (DisciplinesNamesListSerializer,
                             DisciplinesShortSerializer, EventsSerializer,
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


class DisciplinesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Получение списка имён всех спортивных дисциплин.
    """

    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesNamesListSerializer

    def list(self, request, *args, **kwargs):
        disciplines = self.get_queryset()
        names = [discipline.name for discipline in disciplines]
        serializer = DisciplinesNamesListSerializer(data={"names": names})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')


class DisciplinesShortViewSet(mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    """
    Получение краткой информации о спортивной дисциплине
    по названию дисциплины.
    """

    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesShortSerializer
    lookup_field = 'name'

    @swagger_auto_schema(auto_schema=None)
    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')
