from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from core.constants import (MAX_LIST_LENGTH, CustomUserCfg,
                            CustomUserManagerCfg, UserRoleCfg)


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя,
        нормализует email и сохраняет пароль.
        """
        if not email:
            raise ValueError(CustomUserManagerCfg.ERR_MSG_EMAIL)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault(CustomUserManagerCfg.IS_SUPERUSER, False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault(CustomUserManagerCfg.IS_STAFF, True)
        extra_fields.setdefault(CustomUserManagerCfg.IS_SUPERUSER, True)

        if extra_fields.get(CustomUserManagerCfg.IS_SUPERUSER) is not True:
            raise ValueError(CustomUserManagerCfg.ERR_MSG_SUPERUSER)

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Специализированная модель пользователя с расширенными полями.
    Поле phone_number вводить в таком формате +7999 999 99 99
    """
    first_name = models.CharField(
        verbose_name=_(CustomUserCfg.FIRST_NAME_VERBOSE_NAME),
        max_length=CustomUserCfg.MAX_LENGTH_NAME,
        help_text=CustomUserCfg.HELP_MSG_FIRST,
    )
    last_name = models.CharField(
        verbose_name=_(CustomUserCfg.LAST_NAME_VERBOSE_NAME),
        max_length=CustomUserCfg.MAX_LENGTH_NAME,
        help_text=CustomUserCfg.HELP_MSG_LAST,
    )
    phone_number = PhoneNumberField(
        verbose_name=_(CustomUserCfg.PHONE_NUMBER_VERBOSE_NAME),
        unique=True,
        null=False,
        blank=False,
        help_text=CustomUserCfg.HELP_MSG_PHONE)
    email = models.EmailField(
        verbose_name=_(CustomUserCfg.EMAIL_VERBOSE_NAME),
        unique=True,
    )
    role = models.ForeignKey(
        CustomUserCfg.USER_ROLE,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name=CustomUserCfg.ROLE_RELATED_NAME,
        verbose_name=CustomUserCfg.ROLE_VERBOSE_NAME,
        help_text=CustomUserCfg.HELP_MSG_ROLE,
    )

    is_active = models.BooleanField(
        verbose_name=_(CustomUserCfg.IS_ACTIVE_VERBOSE_NAME),
        default=True)
    is_staff = models.BooleanField(
        verbose_name=_(CustomUserCfg.IS_STAFF_VERBOSE_NAME),
        default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = CustomUserCfg.USERNAME_FIELD
    REQUIRED_FIELDS = CustomUserCfg.REQUIRED_FIELDS

    class Meta:
        verbose_name = _(CustomUserCfg.CUSTOM_USER_VERBOSE_NAME)
        verbose_name_plural = _(CustomUserCfg.CUSTOM_USER_VERBOSE_NAME_PLURAL)

    def get_full_name(self):
        """
        Возвращает имя и фамилию с пробелом между ними.
        """
        full_name = f"{self.first_name} {self.last_name}".title()
        return full_name.strip()


class UserRole(models.Model):
    name_role = models.CharField(
        verbose_name=_(UserRoleCfg.NAME_ROLE_VERBOSE_NAME),
        max_length=CustomUserCfg.MAX_LENGTH_NAME,
        unique=True,
        null=False,
        blank=False,
        default=UserRoleCfg.NAME_ROLE_DEFAULT,
    )
    is_active = models.BooleanField(
        verbose_name=_(UserRoleCfg.IS_ACTIVE_VERBOSE_NAME),
        default=True)

    class Meta:
        verbose_name = _(UserRoleCfg.USER_ROLE_VERBOSE_NAME)
        verbose_name_plural = _(UserRoleCfg.USER_ROLE_VERBOSE_NAME_PLURAL)

    def __str__(self) -> str:
        return self.name_role[:MAX_LIST_LENGTH]
