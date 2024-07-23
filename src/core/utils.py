
from django.template.defaultfilters import slugify as django_slugify

from core.constants import ALPHABET, RELATED_NAME_MAP


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


def slugify(s):
    return django_slugify("".join(ALPHABET.get(w, w) for w in s.lower()))
