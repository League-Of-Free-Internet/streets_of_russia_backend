from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import Sports


@admin.register(Sports)
class EventsAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели Виды спорта.
    """
    list_display = (
        'name', 'short_text_preview'
    )
    list_filter = ('name', )
    search_fields = ('name', )

    def short_text_preview(self, obj: Sports) -> str:
        """
        Генерирует краткий текст о виде спорта.
        :param obj: Объект разработчика (экземпляр класса Sports)
        :type obj: Sports

        :return: Краткий текст о виде спорта,
        сокращенной до 50 символов.
        :rtype: str

        """
        return truncatechars(obj.text, 50)

    short_text_preview.short_description = 'Краткий текст'
