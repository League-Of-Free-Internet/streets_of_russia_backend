from django.apps import AppConfig


class EventsConfig(AppConfig):
    """
    Базовая конфигурация для приложения events.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "events"
    verbose_name = "События"
