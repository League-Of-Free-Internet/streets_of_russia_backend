from django.db import models
from django.utils.safestring import mark_safe

from core.constants import (
    MAX_LENGTH,
    MAX_LENGTH_DEFAULT,
    MAX_LIST_LENGTH,
    NewsCfg,
    NewsImageURLCfg,
)
from core.validators import validate_image_url


class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name=NewsCfg.NEWS_NAME_VERBOSE_NAME,
        help_text=NewsCfg.NEWS_NAME_HELP_MSG,
    )
    image_urls = models.ManyToManyField(
        NewsImageURLCfg.NEWS_IMAGE_URL,
        related_name=NewsCfg.NEWS_IMG_URLS_RELATED_NAME,
        verbose_name=NewsCfg.NEWS_IMG_URLS_VERBOSE_NAME,
        help_text=NewsCfg.NEWS_IMG_URLS_HELP_MSG,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=NewsCfg.NEWS_PUB_DATE_VERBOSE_NAME
    )
    description = models.TextField(
        verbose_name=NewsCfg.NEWS_DESCRIPTION_VERBOSE_NAME,
        max_length=MAX_LENGTH,
        help_text=NewsCfg.NEWS_DESCRIPTION_HELP_MSG,
    )

    class Meta:
        ordering = (NewsCfg.NEWS_META_ORDERING_FIELD,)
        verbose_name = NewsCfg.NEWS_META_VERBOSE_NAME
        verbose_name_plural = NewsCfg.NEWS_META_VERBOSE_NAME_PLURAL

    def __str__(self) -> str:
        return self.name[:MAX_LIST_LENGTH]


class NewsImageURL(models.Model):
    news = models.ForeignKey(
        NewsCfg.NEWS,
        on_delete=models.CASCADE,
        related_name=NewsImageURLCfg.NEWS_IMG_URL_FOREIGN_RELATED_NAME,
        verbose_name=NewsImageURLCfg.NEWS_IMG_URL_FOREIGN_VERBOSE_NAME
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name=NewsImageURLCfg.NEWS_IMG_URL_VERBOSE_NAME,
        help_text=NewsImageURLCfg.NEWS_IMG_URL_HELP_MSG,
        validators=(validate_image_url,)
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""

    class Meta:
        verbose_name = NewsImageURLCfg.NEWS_IMG_URL_META_VERBOSE_NAME
        verbose_name_plural = (
            NewsImageURLCfg.NEWS_IMG_URL_META_VERBOSE_NAME_PLURAL
        )

    def __str__(self) -> str:
        return str(self.image_url)
