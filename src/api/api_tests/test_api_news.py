from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api.api_tests.factories import NewsFactory, NewsImageURLFactory


class NewsAPITest(APITestCase):
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

    def test_get_all_news(self):
        url = reverse("news-list")
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.data["count"], 2)
        self.assertIn("news", response.data)
        self.assertEqual(response.data["news"][0]["name"], self.news_2.name,)
        self.assertEqual([self.image_1.image_url],
                         response.data["news"][1]["image_urls"])

    def test_get_news(self):
        url = reverse("news-detail", args=[self.news_1.id])
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.news_1.name)
        self.assertEqual(response.data["description"], self.news_1.description)
        self.assertEqual([self.image_1.image_url], response.data["image_urls"])
