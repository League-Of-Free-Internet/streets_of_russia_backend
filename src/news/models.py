from django.db import models
from django.utils.safestring import mark_safe

from core.constants import MAX_LENGTH_DEFAULT, NewsCfg, MAX_LENGTH


class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="Название новости",
        help_text=NewsCfg.HELP_MSG_NAME,
    )
    image = models.ManyToManyField(
        "ImageURL",
        related_name="images",
        verbose_name="Изображения",
        help_text=NewsCfg.HELP_MSG_IMG,
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    text = models.TextField(
        verbose_name="Содержание новости",
        max_length=MAX_LENGTH,
        help_text=NewsCfg.HELP_MSG_TXT,
    )

    class Meta:
        ordering = ("-date",)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self) -> str:
        return self.name[:25]


class ImageURL(models.Model):
    news = models.ForeignKey(
        "News",
        on_delete=models.CASCADE,
        related_name="news",
        verbose_name="Новость"
    )
    image = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение",
        help_text="Укажите URL-адрес изображения",
    )

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image}" height="50"/>')
        return ""
