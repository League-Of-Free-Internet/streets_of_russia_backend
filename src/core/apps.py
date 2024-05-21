from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Базовая конфигурация для приложения core."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
