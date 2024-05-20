from django.contrib import admin
from django.template.defaultfilters import truncatechars

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели Новости.
    """
    list_display = (
        'name', 'date', 'short_text_preview',
    )
    list_filter = ('date', )
    search_fields = ('name', )

    def short_text_preview(self, obj: News) -> str:
        """
        Генерирует краткий текст новости.
        :param obj: Объект разработчика (экземпляр класса News).
        :type obj: News.

        :return: Краткий текст новости,
        сокращенной до 50 символов.
        :rtype: str.

        """
        return truncatechars(obj.text, 50)

    short_text_preview.short_description = 'Краткий текст'
