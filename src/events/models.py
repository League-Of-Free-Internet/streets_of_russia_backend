from django.db import models
from django.utils.safestring import mark_safe

from core.constants import (MAX_LENGTH, MAX_LENGTH_DEFAULT, EventsCfg,
                            EventsImageURLCfg)


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name=EventsCfg.EVENTS_NAME_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_NAME_HELP_MSG,
    )
    description = models.TextField(
        verbose_name=EventsCfg.EVENTS_DESCRIPTION_VERBOSE_NAME,
        max_length=MAX_LENGTH,
        help_text=EventsCfg.EVENTS_DESCRIPTION_HELP_MSG,
    )
    start_date = models.DateTimeField(
        verbose_name="Дата проведения события"
    )
    image_urls = models.ManyToManyField(
        EventsImageURLCfg.EVENTS_IMAGE_URL,
        related_name=EventsCfg.EVENTS_IMG_RELATED_NAME,
        verbose_name=EventsCfg.EVENTS_IMG_URLS_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_IMG_URLS_HELP_MSG,
    )

    class Meta:
        ordering = ("-start_date",)
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self) -> str:
        return self.name[:25]


class EventsImageURL(models.Model):
    events = models.ForeignKey(
        EventsCfg.EVENTS,
        on_delete=models.CASCADE,
        related_name=EventsImageURLCfg.EVENTS_IMG_URL_FOREIGN_RELATED_NAME,
        verbose_name=EventsImageURLCfg.EVENTS_IMG_URL_VERBOSE_NAME,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name=EventsImageURLCfg.EVENTS_IMG_URL_VERBOSE_NAME,
        help_text=EventsImageURLCfg.EVENTS_IMG_URL_HELP_MSG,
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""
