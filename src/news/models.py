from django.db import models
from django.utils.safestring import mark_safe

from core.constants import (MAX_LENGTH, MAX_LENGTH_DEFAULT, MAX_LIST_LENGTH,
                            NewsCfg)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name=NewsCfg.NAME_VERBOSE_NAME,
        help_text=NewsCfg.HELP_MSG_NAME,
    )
    image_urls = models.ManyToManyField(
        "ImageURL",
        related_name=NewsCfg.IMAGE_URLS_RELATED_NAME,
        verbose_name=NewsCfg.IMAGE_URLS_VERBOSE_NAME,
        help_text=NewsCfg.HELP_MSG_IMG,
    )
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name=NewsCfg.PUB_DATE_VERBOSE_NAME)
    description = models.TextField(
        verbose_name=NewsCfg.DESCRIPTION_VERBOSE_NAME,
        max_length=MAX_LENGTH,
        help_text=NewsCfg.HELP_MSG_TXT,
    )

    class Meta:
        ordering = NewsCfg.ORDERING
        verbose_name = NewsCfg.NEWS_VERBOSE_NAME
        verbose_name_plural = NewsCfg.NEWS_VERBOSE_NAME_PLURAL

    def __str__(self) -> str:
        return self.name[:MAX_LIST_LENGTH]


class ImageURL(models.Model):
    news = models.ForeignKey(
        "News",
        on_delete=models.CASCADE,
        related_name="news",
        verbose_name="Новость"
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение",
        help_text="Укажите URL-адрес изображения",
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""
