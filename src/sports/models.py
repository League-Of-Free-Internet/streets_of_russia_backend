from django.db import models
from django.utils.safestring import mark_safe


class SportsCfg:
    """
    Настройки для модели Sports.
    """

    MAX_LENGTH_DEFAULT = 255
    SPORTS_MAX_LENGTH = 5000
    SPORTS_HELP_MSG_NAME = "Введите название Вида спорта"
    SPORTS_HELP_MSG_TXT = (
        f"Напишите описание вида спорта до {SPORTS_MAX_LENGTH} символов"
    )
    EVENTS_HELP_MSG_IMG = "Добавьте ссылки на изображения с видами спорта"


class Sports(models.Model):
    name = models.CharField(
        max_length=SportsCfg.MAX_LENGTH_DEFAULT,
        verbose_name="Вид спорта",
        help_text=SportsCfg.SPORTS_HELP_MSG_NAME,
    )
    image = models.ManyToManyField(
        "SportsImageURL",
        related_name="sports_images",
        verbose_name="Изображения для событий",
        help_text=SportsCfg.EVENTS_HELP_MSG_IMG,
    )
    text = models.TextField(
        verbose_name="Описание вида спорта",
        max_length=SportsCfg.SPORTS_MAX_LENGTH,
        help_text=SportsCfg.SPORTS_HELP_MSG_TXT,
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
    image = models.URLField(
        max_length=SportsCfg.MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение с видом спорта",
        help_text="Укажите URL-адрес изображения с видом спорта",
    )

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image}" height="50"/>')
        return ""
