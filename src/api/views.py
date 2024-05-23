from rest_framework import viewsets

from news.models import News


class NewsViewSet(viewsets.ModelViewSet):
    """
    Реализует операции с моделью News:
    - получения списка новостей;
    - создание новой новости;
    - редактирование новости;
    - удаление новости.
    """
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = News.objects.all()
    search_fields = ('name',)
    lookup_field = 'name'
