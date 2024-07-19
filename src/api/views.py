from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from api.pagination import NewsPagination
from api.serializers import (DisciplinesFullSerializer,
                             DisciplinesNamesListSerializer,
                             DisciplinesShortSerializer, EventSerializer,
                             EventSignUpSerializer, FourLatestEventsSerializer,
                             NewsSerializer, UserSerializer)
from core.constants import EVENTS_ORDER, NEWS_ORDER, PAGE
from disciplines.models import Disciplines
from events.models import Events, EventSignUp
from news.models import News
from users.models import CustomUser


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Реализует операции с моделью News:
    - получения списка новостей;
    - получение информации о конкретной новости;
    Работает с пагинацией на 12 новостей на каждой странице.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
    lookup_field = "id"

    def get_queryset(self):
        """
        Если получаемый GET-запрос относится к действию list и не заданы
        настройки для пагинации, тогда выводит список последних 3 новостей.
        Если получаемый GET-запрос относится к действию list и заданы
        настройки для пагинации, тогда выводит список последних 12 новостей.
        Если получаемый GET-запрос относится к действию retrieve, тогда выводит
        конкретную новость по id.
        """
        if self.action == "list" and PAGE not in self.request.query_params:
            return News.objects.order_by(NEWS_ORDER)[:3]
        if self.action == "retrieve":
            return News.objects.filter(id=self.kwargs.get('id'))
        return super().get_queryset()


class UserViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для создания пользовательских
    экземпляров с использованием метода POST
    при регистрации участника.

    Этот набор представлений поддерживает
    только действие `создать` для метода POST.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ("post",)


class FourLatestEventsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Реализует операцию List с моделью Events. Только для администратора.
    """

    queryset = Events.objects.all()
    serializer_class = FourLatestEventsSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        """
        Возвращает последние 4 экземпляра модели Events.
        """
        return Events.objects.order_by(EVENTS_ORDER)[:4]


class EventViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Реализует операцию Retrieve с моделью Events.
    """

    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    lookup_field = "id"


class EventSignUpViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Реализует операцию Create с моделью EventSignUp.
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


class DisciplinesNamesListViewSet(mixins.ListModelMixin,
                                  viewsets.GenericViewSet):
    """
    Реализует операцию List с моделью Disciplines.
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


class DisciplinesShortViewSet(mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    """
    Реализует операцию Retrieve с моделью Disciplines.
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
