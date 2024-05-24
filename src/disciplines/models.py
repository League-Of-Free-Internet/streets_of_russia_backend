from django.db import models
from django.utils.safestring import mark_safe

from core.constants import (MAX_LENGTH, MAX_LENGTH_DEFAULT, DisciplinesCfg,
                            DisciplinesImageURLCfg)


class Disciplines(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name=DisciplinesCfg.DISCIPLINES_NAME_VERBOSE_NAME,
        help_text=DisciplinesCfg.DISCIPLINES_NAME_HELP_MSG,
        unique=True
    )
    description = models.TextField(
        verbose_name=DisciplinesCfg.DISCIPLINES_DESCRIPTION_VERBOSE_NAME,
        max_length=MAX_LENGTH,
        help_text=DisciplinesCfg.DISCIPLINES_DESCRIPTION_HELP_MSG,
    )
    image_urls = models.ManyToManyField(
        DisciplinesImageURLCfg.DISCIPLINES_IMG_URL,
        related_name=DisciplinesCfg.DISCIPLINES_IMG_URLS_RELATED_NAME,
        verbose_name=DisciplinesCfg.DISCIPLINES_IMG_URLS_VERBOSE_NAME,
        help_text=DisciplinesCfg.DISCIPLINES_IMG_URLS_HELP_MSG,
    )
    rules = models.TextField(
        verbose_name=DisciplinesCfg.DISCIPLINES_RULES_VERBOSE_NAME,
        max_length=MAX_LENGTH,
        help_text=DisciplinesCfg.DISCIPLINES_RULES_HELP_MSG,
    )

    class Meta:
        ordering = (DisciplinesCfg.DISCIPLINES_META_ORDERING_FIELD,)
        verbose_name = DisciplinesCfg.DISCIPLINES_META_VERBOSE_NAME
        verbose_name_plural = (
            DisciplinesCfg.DISCIPLINES_META_VERBOSE_NAME_PLURAL
        )

    def __str__(self) -> str:
        return self.name[:25]


class DisciplinesImageURL(models.Model):
    name = models.ForeignKey(
        DisciplinesCfg.DISCIPLINES,
        on_delete=models.CASCADE,
        related_name=(
            DisciplinesImageURLCfg.DISCIPLINES_IMG_URL_FOREIGN_RELATED_NAME
        ),
        verbose_name=(
            DisciplinesImageURLCfg.DISCIPLINES_IMG_URL_FOREIGN_VERBOSE_NAME
        )
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name=DisciplinesImageURLCfg.DISCIPLINES_IMG_URL_VERBOSE_NAME,
        help_text=DisciplinesImageURLCfg.DISCIPLINES_IMG_URL_HELP_MSG,
    )

    def image_tag(self):
        if self.image_url is not None:
            return mark_safe(f'<img src="{self.image_url}" height="50"/>')
        return ""
