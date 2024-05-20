from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели События.
    """
    list_display = (
        'name', 'date', 'short_text_preview',
    )
    list_filter = ('date', )
    search_fields = ('name', )

    def short_text_preview(self, obj: Events) -> str:
        """
        Генерирует краткий текст события.
        :param obj: Объект разработчика (экземпляр класса Events)
        :type obj: Events

        :return: Краткий текст новости,
        сокращенной до 50 символов.
        :rtype: str

        """
        return truncatechars(obj.text, 50)

    short_text_preview.short_description = 'Краткий текст'
