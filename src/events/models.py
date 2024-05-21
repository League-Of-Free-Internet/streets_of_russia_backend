from django.db import models
from django.utils.safestring import mark_safe


class EventsCfg:
    """
    Настройки для модели Events.
    """

    MAX_LENGTH_DEFAULT = 255
    EVENTS_MAX_LENGTH = 5000
    EVENTS_HELP_MSG_NAME = "Введите название События"
    EVENTS_HELP_MSG_TXT = (
        f"Напишите текст события до {EVENTS_MAX_LENGTH} символов"
    )
    EVENTS_HELP_MSG_IMG = "Добавьте ссылки на изображения с событиями"


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=EventsCfg.MAX_LENGTH_DEFAULT,
        verbose_name="Событие",
        help_text=EventsCfg.EVENTS_HELP_MSG_TXT,
    )
    image = models.ManyToManyField(
        "EventsImageURL",
        related_name="events_images",
        verbose_name="Изображения для событий",
        help_text=EventsCfg.EVENTS_HELP_MSG_IMG,
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата события"
    )
    text = models.TextField(
        verbose_name="Содержание события",
        max_length=EventsCfg.EVENTS_MAX_LENGTH,
        help_text=EventsCfg.EVENTS_HELP_MSG_TXT,
    )

    class Meta:
        ordering = ("date",)
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self) -> str:
        return self.name[:25]


class EventsImageURL(models.Model):
    news = models.ForeignKey(
        "Events",
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name="События",
    )
    image = models.URLField(
        max_length=EventsCfg.MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение",
        help_text="Укажите URL-адрес изображения",
    )

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image}" height="50"/>')
        return ""
