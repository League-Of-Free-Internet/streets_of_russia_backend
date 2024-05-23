from django.db import models
from django.utils.safestring import mark_safe

from core.constants import MAX_LENGTH, MAX_LENGTH_DEFAULT, EventsCfg


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="Событие",
        help_text=EventsCfg.EVENTS_HELP_MSG_NAME,
    )
    description = models.TextField(
        verbose_name="Содержание события",
        max_length=MAX_LENGTH,
        help_text=EventsCfg.EVENTS_HELP_MSG_TXT,
    )
    start_date = models.DateTimeField(
        verbose_name="Дата проведения события"
    )
    image_urls = models.ManyToManyField(
        "EventsImageURL",
        related_name="events_images",
        verbose_name="Изображения для событий",
        help_text=EventsCfg.EVENTS_HELP_MSG_IMG,
    )

    class Meta:
        ordering = ("-start_date",)
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
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение события",
        help_text="Укажите URL-адрес изображения о событии",
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""
