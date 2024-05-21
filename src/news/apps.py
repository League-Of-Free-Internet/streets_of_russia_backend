from django.apps import AppConfig


class NewsConfig(AppConfig):
    """
    Базовая конфигурация для приложения news.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "news"
    verbose_name = "Новости"
