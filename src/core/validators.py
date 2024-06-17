import re

import requests
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import status

from core.constants import MediaValidatorCfg


def validate_image_url(url):
    try:
        URLValidator(url)
    except ValidationError:
        raise ValidationError(MediaValidatorCfg.URL_ERR_MSG)
    try:
        response = requests.head(url)
        content_type = response.headers.get(MediaValidatorCfg.CONTENT_TYPE)
        if response.status_code != status.HTTP_200_OK:
            raise ValidationError(MediaValidatorCfg.ACCESS_ERR_MSG
                                  + f"Ошибка {response.status_code}")
        if MediaValidatorCfg.IMAGE not in content_type:
            raise ValidationError(MediaValidatorCfg.URL_ERR_IMG)
    except requests.RequestException:
        raise ValidationError(MediaValidatorCfg.ACCESS_ERR_MSG)


def validate_url_video(url):
    try:
        URLValidator(url)
    except ValidationError:
        raise ValidationError(MediaValidatorCfg.URL_ERR_MSG)
    try:
        response = requests.head(url)
        content_type = response.headers.get(MediaValidatorCfg.CONTENT_TYPE)
        if (MediaValidatorCfg.VIDEO not in content_type
                and not re.match(MediaValidatorCfg.YT_REGEX, url)):
            raise ValidationError(MediaValidatorCfg.URL_ERR_VID)
    except requests.RequestException:
        raise ValidationError(MediaValidatorCfg.ACCESS_ERR_MSG)
