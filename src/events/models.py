from django.db import models


class EventsCfg:
    """
    Настройки для модели Events.
    """
    ID_MAX_LENGTH = 5
    MAX_LENGTH_DEFAULT = 255
    EVENTS_MAX_LENGTH = 5000
    EVENTS_HELP_MSG_NAME = 'Введите название События'
    EVENTS_HELP_MSG_TXT = f'Напишите текст события до {EVENTS_MAX_LENGTH} символов'


class Events(models.Model):
    id = models.IntegerField(
        max_length=EventsCfg.ID_MAX_LENGTH,
        verbose_name="id для создания ссылки",
        unique=True
    )
    name = models.CharField(
        max_length=EventsCfg.MAX_LENGTH_DEFAULT,
        verbose_name='Событие',
        help_text=EventsCfg.EVENTS_HELP_MSG_TXT
    )
    image = models.URLField(
        max_length=EventsCfg.MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name='Ссылка на изображение с событием')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата события'
    )
    text = models.TextField(
        verbose_name='Содержание новости',
        max_length=EventsCfg.EVENTS_MAX_LENGTH,
        help_text=EventsCfg.EVENTS_HELP_MSG_TXT
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
