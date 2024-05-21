from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import Sports, SportsImageURL


class SportsImageURLInline(admin.TabularInline):
    """
    Позволяет отображать и добавлять несколько URL-ссылок для видов спорта
    в виде горизонтального расположения.
    """

    model = SportsImageURL
    extra = 1
    readonly_fields = ("image_tag",)
    verbose_name = "Изображение с видом спорта"
    verbose_name_plural = "Изображения с видом спорта"
    SportsImageURL.image_tag.short_description = "Миниатюра"


@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели Виды спорта.
    """

    exclude = ("image",)
    inlines = (SportsImageURLInline,)
    list_display = (
        "name",
        "short_text_preview"
    )
    list_filter = ("name",)
    search_fields = ("name",)

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

    short_text_preview.short_description = "Краткий текст"
