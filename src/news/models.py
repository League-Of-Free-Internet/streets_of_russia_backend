from django.db import models


class News(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Новости',
    )
    image = models.ImageField(
        upload_to='media',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    url_image = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Ссылка на изображение')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата',)
    text = models.TextField(
        verbose_name='Содержание новости',
    )
