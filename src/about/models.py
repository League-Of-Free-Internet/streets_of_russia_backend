from django.db import models

from core.constants import (MAX_LENGTH, MAX_LENGTH_DEFAULT, MAX_LIST_LENGTH,
                            AboutCfg, BannerVideoCfg, OurMemberCfg)


class BannerVideo(models.Model):
    id = models.AutoField(primary_key=True)
    video_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name=BannerVideoCfg.VIDEO_URL_VERBOSE_NAME,
        help_text=BannerVideoCfg.HELP_MSG_VIDEO,
    )

    class Meta:
        verbose_name = BannerVideoCfg.BANNER_VIDEO_VERBOSE_NAME
        verbose_name_plural = BannerVideoCfg.BANNER_VIDEO_VERBOSE_NAME_PLURAL


class OurMembers(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(
        OurMemberCfg.ROLE_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name=OurMemberCfg.ROLE_RELATED_NAME,
        verbose_name=OurMemberCfg.ROLE_VERBOSE_NAME,
        help_text=AboutCfg.HELP_MSG_ROLE,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name=OurMemberCfg.IMAGE_URL_VERBOSE_NAME,
        help_text=OurMemberCfg.IMAGE_URL_HELP_TEXT,
    )
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name=OurMemberCfg.NAME_VERBOSE_NAME,
        help_text=AboutCfg.HELP_MSG_NAME,
    )
    text = models.TextField(
        verbose_name=OurMemberCfg.TEXT_VERBOSE_NAME,
        max_length=MAX_LENGTH,
        help_text=OurMemberCfg.TEXT_HELP_MSG,
    )

    class Meta:
        verbose_name = OurMemberCfg.OUR_MEMBERS_VERBOSE_NAME
        verbose_name_plural = OurMemberCfg.OUR_MEMBERS_VERBOSE_NAME_PLURAL

    def __str__(self) -> str:
        return self.name[:MAX_LIST_LENGTH]


class MemberRole(models.Model):
    name = models.CharField(
        verbose_name="Название роли",
        max_length=AboutCfg.MAX_LENGTH_NAME,
        unique=True,
        null=False,
        blank=False,
        default="Общественный деятель",
    )
    is_active = models.BooleanField(
        verbose_name="Роль активна",
        default=True)

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self) -> str:
        return self.name[:MAX_LIST_LENGTH]


class About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Подробное описание",
        max_length=MAX_LENGTH,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Ссылка на изображение",
        help_text=AboutCfg.HELP_MSG_IMG,
    )

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self) -> str:
        return self.name[:MAX_LIST_LENGTH]


class PartnerLogo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="Название",
        help_text=AboutCfg.HELP_MSG_PARTNER,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение",
        help_text=AboutCfg.HELP_MSG_IMG,
    )

    class Meta:
        verbose_name = "Логотип партнера"
        verbose_name_plural = "Логотипы партнеров"


class BrandBook(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="Название",
        unique=True,
        blank=False,
        null=False,
        help_text=AboutCfg.HELP_MSG_BRAND,
    )
    file = models.FileField(
        upload_to='brandbook'
    )
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Дата")
    is_active = models.BooleanField(
        verbose_name="Брендбук активен",
        default=True)

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Брендбук"
        verbose_name_plural = "Брендбуки"

    def __str__(self) -> str:
        return self.name[:MAX_LIST_LENGTH]
