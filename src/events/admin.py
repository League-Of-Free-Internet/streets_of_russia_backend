from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import Events, EventsImageURL


class EventsImageURLInline(admin.TabularInline):
    """
    Позволяет отображать и добавлять несколько URL-ссылок для событий
    в виде горизонтального расположения.
    """

    model = EventsImageURL
    extra = 1
    readonly_fields = (
        "id",
        "image_tag"
    )
    verbose_name = "Изображение о событии"
    verbose_name_plural = "Изображения о событии"
    EventsImageURL.image_tag.short_description = "Миниатюра"


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели События.
    """

    exclude = ("image_urls",)
    inlines = (EventsImageURLInline,)
    list_display = (
        "name",
        "start_date",
        "short_text_preview",
    )
    list_filter = ("start_date",)
    search_fields = ("name",)

    def short_text_preview(self, obj: Events) -> str:
        """
        Генерирует краткий текст события.
        :param obj: Объект разработчика (экземпляр класса Events)
        :type obj: Events

        :return: Краткий текст новости,
        сокращенной до 50 символов.
        :rtype: str

        """
        return truncatechars(obj.description, 50)

    short_text_preview.short_description = "Краткий текст"
