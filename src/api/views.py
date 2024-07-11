from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from api.pagination import NewsPagination
from api.serializers import (DisciplinesFullSerializer,
                             DisciplinesNamesListSerializer,
                             DisciplinesShortSerializer, EventSerializer,
                             EventSignUpSerializer, FourLatestEventsSerializer,
                             NewsSerializer, UserSerializer)
from core.constants import EVENTS_ORDER_FIELD
from disciplines.models import Disciplines
from events.models import Events, EventSignUp
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


class FourLatestEventsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Получение списка 4 последних событий. Только для администратора.
    """

    queryset = Events.objects.all()
    pagination_class = None
    serializer_class = FourLatestEventsSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        """
        Возвращает последние 4 экземпляра модели Events.
        """
        return Events.objects.order_by(EVENTS_ORDER_FIELD)[:4]

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        """
        Запрет на получение конкретного события по id на данном эндпоинте.
        """
        raise MethodNotAllowed("GET")


class EventViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Получение информации о конкретном событии.
    """

    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    lookup_field = "id"


class EventSignUpViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Запись пользователя на конкретное событие.
    """

    queryset = EventSignUp.objects.all()
    serializer_class = EventSignUpSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_event(self):
        """
        Получение события по переданному event_id.
        """
        return Events.objects.get(id=self.kwargs.get("event_id"))

    def create(self, request, *args, **kwargs):
        """
        Создание записи текущего пользователя на конкретное событие.
        В случае повторного POST-запроса - удаление записи из БД.
        В теле запроса поле data должно оставаться пустым.
        """
        event = self.get_event()
        user = self.request.user
        registration = EventSignUp.objects.filter(
            user=user, event=event
        ).first()
        if registration:
            registration.delete()
            return Response(
                {"message": "Вы отменили регистрацию на событие"},
                status=status.HTTP_200_OK
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )

    def perform_create(self, serializer):
        """
        Сохранение записи текущего пользователя на конкретное событие.
        """
        serializer.save(user=self.request.user, event=self.get_event())


class DisciplinesNamesListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Работа со всеми спортивными дисциплинами.
    """

    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesNamesListSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    lookup_field = "id"

    def list(self, request, *args, **kwargs):
        """
        Получение списка имен существующих спортивных дисциплин.
        """
        disciplines = self.get_queryset()
        names = [discipline.name for discipline in disciplines]
        serializer = DisciplinesNamesListSerializer(data={"names": names})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        """
        Запрет на получение конкретной спортивной дисциплины по id
        на данном эндпоинте.
        """
        raise MethodNotAllowed("GET")


class DisciplinesShortViewSet(mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    """
    Получение краткой информации о спортивной дисциплине
    по названию дисциплины.
    """

    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesShortSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    lookup_field = "name"


class DisciplinesFullViewSet(mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    """
    Получение полной информации о спортивной дисциплине
    по названию дисциплины.
    """

    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesFullSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    lookup_field = "name"
