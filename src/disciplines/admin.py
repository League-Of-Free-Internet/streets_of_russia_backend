from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import Disciplines, DisciplinesImageURL


class DisciplinesImageURLInline(admin.TabularInline):
    """
    Позволяет отображать и добавлять несколько URL-ссылок для видов спорта
    в виде горизонтального расположения.
    """

    model = DisciplinesImageURL
    extra = 1
    readonly_fields = ("image_tag",)
    verbose_name = "Изображение с видом спорта"
    verbose_name_plural = "Изображения с видом спорта"
    DisciplinesImageURL.image_tag.short_description = "Миниатюра"


@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели Виды спорта.
    """

    exclude = ("image_urls",)
    inlines = (DisciplinesImageURLInline,)
    list_display = (
        "name",
        "short_text_preview"
    )
    list_filter = ("name",)
    search_fields = ("name",)

    def short_text_preview(self, obj: Disciplines) -> str:
        """
        Генерирует краткий текст о спортивной дисциплине.
        :param obj: Объект разработчика (экземпляр класса Disciplines)
        :type obj: Disciplines
        :return: Краткий текст о спортивной дисциплине,
        сокращенной до 50 символов.
        :rtype: str
        """
        return truncatechars(obj.description, 50)

    short_text_preview.short_description = "Краткий текст"
