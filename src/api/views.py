from rest_framework import viewsets, permissions

from api.serializers import UserSerializer, NewsSerializer

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
    http_method_names = ("get", "post", "patch", "delete")
    search_fields = ("name",)
    lookup_field = "name"


class UserViewSet(viewsets.ModelViewSet):
    """Работа с пользователями. Только для администратора."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)
    lookup_field = "email"
    search_fields = ("email",
                     "phone_number",
                     "first_name",
                     "last_name")
    http_method_names = ("get", "post",
                         "patch", "delete")


class SignUpViewSet():
    ...
