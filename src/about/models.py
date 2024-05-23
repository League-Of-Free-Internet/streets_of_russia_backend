from django.db import models

from core.constants import MAX_LENGTH, MAX_LENGTH_DEFAULT, AboutCfg


class BannerVideo(models.Model):
    id = models.AutoField(primary_key=True)
    video_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на видео",
        help_text="Укажите URL-адрес видео",
    )


class OurMembers(models.Model):
    class Role(models.TextChoices):
        """Список доступных значений для поля "роль"."""

        MEMBER = 'ME', 'Участник'
        PARTNER = 'PA', 'Партнёр'
        PUBLIC_FIGURE = 'PF', 'Общественный деятель'
        VOLUNTEER = 'MO', 'Модератор'
        ADMIN = 'AD', 'Администратор'
    id = models.AutoField(primary_key=True)
    role = models.CharField(
        verbose_name='Роль',
        max_length=MAX_LENGTH_DEFAULT,
        blank=False,
        choices=Role.choices,
        default=Role.MEMBER,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение",
        help_text="Укажите URL-адрес изображения",
    )
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="Имя",
        help_text=AboutCfg.HELP_MSG_NAME,
    )
    text = models.TextField(
        verbose_name="История участника",
        max_length=MAX_LENGTH,
        help_text=AboutCfg.HELP_MSG_TXT,
    )


class About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="название",
        help_text=...,
    )
    description = models.TextField(
        verbose_name="Описание вида спорта",
        max_length=MAX_LENGTH,
        help_text=...,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Ссылка на изображение",
        help_text="Укажите URL-адрес изображения",
    )


class PartnerLogo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=MAX_LENGTH_DEFAULT,
        verbose_name="название",
        help_text=...,
    )
    image_url = models.URLField(
        max_length=MAX_LENGTH_DEFAULT,
        unique=True,
        verbose_name="Ссылка на изображение",
        help_text="Укажите URL-адрес изображения",
    )
