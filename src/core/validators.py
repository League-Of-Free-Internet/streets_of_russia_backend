import requests
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import status


def validate_image_url(url):
    try:
        URLValidator(url)
    except ValidationError:
        raise ValidationError("Укажите корректный URL-адрес")
    try:
        response = requests.head(url)
        content_type = response.headers.get("content-type")
        if response.status_code != status.HTTP_200_OK:
            raise ValidationError("Не удалось получить доступ к ссылке. "
                                  f"Ошибка {response.status_code}")
        if "image" not in content_type:
            raise ValidationError("URL-адрес не указывает на изображение")
    except requests.RequestException:
        raise ValidationError("Не удалось получить доступ к ссылке.")
