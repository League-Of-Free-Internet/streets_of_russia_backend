from news.models import News
from rest_framework import viewsets


class NewsViewSet(viewsets.ModelViewSet):
    """
    Реализует операции с моделью CustomUser:
    - получения списка пользователей;
    - создание пользователя;
    - получение детализации по пользователю;
    - редактирование пользователя;
    - удаление пользователя.
    """
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = News.objects.all()
    search_fields = ('name',)
    lookup_field = 'name'
