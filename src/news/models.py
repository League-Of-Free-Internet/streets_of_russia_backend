from django.db import models
from django.utils.safestring import mark_safe


class NewsCfg:
    """
    Настройки для модели News.
    """

    MAX_LENGTH_DEFAULT = 255
    NEWS_MAX_LENGTH = 5000
    HELP_MSG_NAME = "Введите название Новости"
    HELP_MSG_TXT = f"Напишите текст новости до {NEWS_MAX_LENGTH} символов"
    HELP_MSG_IMG = "Добавьте ссылки на изображения"


class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=NewsCfg.MAX_LENGTH_DEFAULT,
        verbose_name="Название новости",
        help_text=NewsCfg.HELP_MSG_NAME,
    )
    image_urls = models.ManyToManyField(
        "ImageURL",
        related_name="images",
        verbose_name="Изображения",
        help_text=NewsCfg.HELP_MSG_IMG,
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    text = models.TextField(
        verbose_name="Содержание новости",
        max_length=NewsCfg.NEWS_MAX_LENGTH,
        help_text=NewsCfg.HELP_MSG_TXT,
    )

    class Meta:
        ordering = ("-pub_date",)
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
    image_url = models.URLField(
        max_length=NewsCfg.MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение",
        help_text="Укажите URL-адрес изображения",
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""
