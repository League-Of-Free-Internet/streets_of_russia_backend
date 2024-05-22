from django.db import models
from django.utils.safestring import mark_safe

from core.constants import MAX_LENGTH_DEFAULT, SportsCfg, MAX_LENGTH


class Sports(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="Вид спорта",
        help_text=SportsCfg.SPORTS_HELP_MSG_NAME,
    )
    image_urls = models.ManyToManyField(
        "SportsImageURL",
        related_name="sports_images",
        verbose_name="Изображения для событий",
        help_text=SportsCfg.EVENTS_HELP_MSG_IMG,
    )
    description = models.TextField(
        verbose_name="Описание вида спорта",
        max_length=MAX_LENGTH,
        help_text=SportsCfg.SPORTS_HELP_MSG_TXT,
    )
    rules = models.TextField(
        verbose_name="Правила вида спорта",
        max_length=MAX_LENGTH,
        help_text=SportsCfg.SPORTS_RULES_HELP_MSG_TXT,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"

    def __str__(self) -> str:
        return self.name[:25]


class SportsImageURL(models.Model):
    news = models.ForeignKey(
        "Sports",
        on_delete=models.CASCADE,
        related_name="sports",
        verbose_name="Виды спорта",
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение с видом спорта",
        help_text="Укажите URL-адрес изображения с видом спорта",
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""
