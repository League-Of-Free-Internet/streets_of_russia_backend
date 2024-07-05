from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from core.constants import (MAX_LENGTH, MAX_LENGTH_DEFAULT, MAX_LIST_LENGTH,
                            EventsCfg, EventsImageURLCfg)
from core.validators import validate_image_url


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
    image_urls = models.ManyToManyField(
        EventsImageURLCfg.EVENTS_IMAGE_URL,
        related_name=EventsCfg.EVENTS_IMG_RELATED_NAME,
        verbose_name=EventsCfg.EVENTS_IMG_URLS_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_IMG_URLS_HELP_MSG,
    )
    start_date = models.DateTimeField(
        verbose_name=EventsCfg.EVENTS_START_DATE_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_START_DATE_HELP_MSG,
        default=timezone.now,
    )
    place = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name=EventsCfg.EVENTS_PLACE_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_PLACE_HELP_MSG,
    )
    rules = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name=EventsCfg.EVENTS_RULES_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_RULES_HELP_MSG,
    )
    deadline_registration_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=EventsCfg.EVENTS_DEADLINE_REG_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_DEADLINE_REG_HELP_MSG
    )
    discipline = models.ForeignKey(
        EventsCfg.EVENTS_DISCIPLINE_FOREIGN_KEY,
        on_delete=models.CASCADE,
        related_name=EventsCfg.EVENTS_DISCIPLINE_RELATED_NAME,
        verbose_name=EventsCfg.EVENTS_DISCIPLINE_VERBOSE_NAME,
        help_text=EventsCfg.EVENTS_DISCIPLINE_HELP_MSG,
    )

    class Meta:
        ordering = (EventsCfg.EVENTS_META_ORDERING_FIELD,)
        verbose_name = EventsCfg.EVENTS_META_VERBOSE_NAME
        verbose_name_plural = EventsCfg.EVENTS_META_VERBOSE_NAME_PLURAL

    def __str__(self) -> str:
        return self.name[:MAX_LIST_LENGTH]


class EventsImageURL(models.Model):
    events = models.ForeignKey(
        EventsCfg.EVENTS,
        on_delete=models.CASCADE,
        related_name=EventsImageURLCfg.EVENTS_IMG_URL_FOREIGN_RELATED_NAME,
        verbose_name=EventsImageURLCfg.EVENTS_IMG_URL_FOREIGN_VERBOSE_NAME,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name=EventsImageURLCfg.EVENTS_IMG_URL_VERBOSE_NAME,
        help_text=EventsImageURLCfg.EVENTS_IMG_URL_HELP_MSG,
        validators=(validate_image_url,)
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""

    class Meta:
        verbose_name = EventsImageURLCfg.EVENTS_IMG_URL_META_VERBOSE_NAME
        verbose_name_plural = (
            EventsImageURLCfg.EVENTS_IMG_URL_META_VERBOSE_NAME_PLURAL
        )

    def __str__(self) -> str:
        return str(self.image_url)
