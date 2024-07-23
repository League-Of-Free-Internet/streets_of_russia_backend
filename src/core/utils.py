from rest_framework.exceptions import NotFound

from core.constants import RELATED_NAME_MAP
from events.models import Events


def get_image_urls(obj):
    """
    Функция для получения списка всех url-изображений для каждой переданной
    модели.
    """
    model_name = obj.__class__.__name__
    related_name = RELATED_NAME_MAP.get(model_name)
    if not related_name:
        raise ValueError(
            f"Нет related_name для полученной модели {model_name}"
        )
    image_urls = getattr(obj, related_name).all()
    return [url.image_url for url in image_urls]


def get_event(event_id):
    """
    Получение события по переданному event_id.
    """
    try:
        return Events.objects.get(id=event_id)
    except Events.DoesNotExist:
        raise NotFound("Событие не найдено.")
