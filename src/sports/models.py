from django.db import models


class SportsCfg:
    """
    Настройки для модели Sports.
    """
    MAX_LENGTH_DEFAULT = 255
    SPORTS_MAX_LENGTH = 5000
    SPORTS_HELP_MSG_NAME = 'Введите название Вида спорта'
    SPORTS_HELP_MSG_TXT = (
        f'Напишите описание вида спорта до {SPORTS_MAX_LENGTH} символов'
    )


class Sports(models.Model):
    name = models.CharField(
        max_length=SportsCfg.MAX_LENGTH_DEFAULT,
        verbose_name='Вид спорта',
        help_text=SportsCfg.SPORTS_HELP_MSG_NAME
    )
    image = models.URLField(
        max_length=SportsCfg.MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name='Ссылка на изображение с видом спорта'
    )
    text = models.TextField(
        verbose_name='Описание вида спорта',
        max_length=SportsCfg.SPORTS_MAX_LENGTH,
        help_text=SportsCfg.SPORTS_HELP_MSG_TXT
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'
