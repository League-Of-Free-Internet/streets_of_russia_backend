from django.db import models


class NewsCfg:
    """
    Настройки для модели News
    """
    MAX_LENGTH_DEFAULT = 255
    NEWS_MAX_LENGHT = 5000
    HELP_MSG_NAME = 'Введите название Новости'
    HELP_MSG_TXT = f'Напишите текст новости до {NEWS_MAX_LENGHT} символов'


class News(models.Model):
    name = models.CharField(
        max_length=NewsCfg.MAX_LENGTH_DEFAULT,
        verbose_name='Новости',
        help_text=NewsCfg.HELP_MSG_NAME
    )
    image = models.ImageField(
        upload_to='media',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    url_image = models.URLField(
        max_length=NewsCfg.MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name='Ссылка на изображение')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата',)
    text = models.TextField(
        verbose_name='Содержание новости',
        max_length=NewsCfg.NEWS_MAX_LENGHT,
        help_text=NewsCfg.HELP_MSG_TXT
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
