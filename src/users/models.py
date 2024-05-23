from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from core.constants import CustomUserCfg


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя,
        нормализует email и сохраняет пароль.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Специализированная модель пользователя с расширенными полями.
    phone_number: вводить в таком формете +7999 999 99 99
    """
    first_name = models.CharField(
        verbose_name=_("Имя"),
        max_length=CustomUserCfg.MAX_LENGTH_NAME,
        help_text=CustomUserCfg.HELP_MSG_FIRST,
    )
    last_name = models.CharField(
        verbose_name=_("Фамилия"),
        max_length=CustomUserCfg.MAX_LENGTH_NAME,
        help_text=CustomUserCfg.HELP_MSG_LAST,
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Номер телефона"),
        unique=True,
        null=False,
        blank=False,
        help_text=CustomUserCfg.HELP_MSG_PHONE)
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True,
    )
    role = models.ForeignKey(
        "UserRole",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="users",
        verbose_name="Роль",
        help_text=CustomUserCfg.HELP_MSG_ROLE,
    )

    is_active = models.BooleanField(
        verbose_name=_("Аккаунт активен"),
        default=True)
    is_staff = models.BooleanField(
        verbose_name=_("Является персоналом"),
        default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("phone_number", )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        """
        Возвращает имя и фамилию с пробелом между ними.
        """
        full_name = f"{self.first_name} {self.last_name}".title()
        return full_name.strip()


class UserRole(models.Model):
    name_role = models.CharField(
        verbose_name=_("Название роли"),
        max_length=CustomUserCfg.MAX_LENGTH_NAME,
        unique=True,
        null=False,
        blank=False,
        default="Участник",
    )
    is_active = models.BooleanField(
        verbose_name=_("Роль активна"),
        default=True)
