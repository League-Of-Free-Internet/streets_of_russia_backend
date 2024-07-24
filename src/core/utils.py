from django.http import JsonResponse
from django.template.defaultfilters import slugify as django_slugify
from rest_framework import status
from rest_framework.views import exception_handler

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


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data["status_code"] = response.status_code
        response.data["error_message"] = response.data.pop("detail", None)
    return response


def not_found(request, exception, *args, **kwargs):
    """
    Общий 404 обработчик ошибок.
    """
    data = {
        "status_code": 404,
        "error_message": "Запрашиваемый ресурс не найден (404)"
    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND,
                        json_dumps_params={"ensure_ascii": False})


def server_error(request, *args, **kwargs):
    """
    Общий 500 обработчик ошибок.
    """
    data = {
        "status_code": 500,
        "error": "Ошибка сервера (500)"
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        json_dumps_params={"ensure_ascii": False})


def bad_request(request, exception, *args, **kwargs):
    """
    Общий 400 обработчик ошибок.
    """
    data = {
        "status_code": 400,
        "error": "Плохой запрос (400)"
    }
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST,
                        json_dumps_params={"ensure_ascii": False})


def forbidden(request, exception, *args, **kwargs):
    """
    Общий 400 обработчик ошибок.
    """
    data = {
        "status_code": 403,
        "error": "Доступ запрещён (403)"
    }
    return JsonResponse(data, status=status.HTTP_403_FORBIDDEN,
                        json_dumps_params={"ensure_ascii": False})
