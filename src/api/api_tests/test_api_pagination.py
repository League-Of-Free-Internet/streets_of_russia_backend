from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from news.models import News, NewsImageURL


class PaginationAPITest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.api_client = APIClient()
        cls.news_1 = NewsFactory.create_news(
            "Тестовая Новость 1",
            "Обычный текст 1",)
        cls.news_2 = NewsFactory.create_news(
            "Тестовая Новость 2",
            "Обычный текст 2",)
        cls.image_1 = NewsImageURLFactory.create_news_image_url(
            cls.news_1, "https://clck.ru/3AjpaT"
        )
        cls.image_2 = NewsImageURLFactory.create_news_image_url(
            cls.news_2, "https://clck.ru/3BzJUK"
        )

        cls.image_3 = NewsImageURLFactory.create_news_image_url(
            cls.news_2, "https://clck.ru/3BzXGE"
        )