from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.api_tests.factories import NewsFactory, NewsImageURLFactory


class PaginationAPITest(APITestCase):
    def setUp(self):
        self.news_batch = NewsFactory.create_news_batch(100)
        self.image_urls_batch = NewsImageURLFactory.create_image_urls_batch(
            news_batch=self.news_batch
        )
        self.response = self.client.get(reverse("news-list"))

    def tearDown(self):
        [news.delete() for news in self.news_batch]
        [image_urls.delete() for image_urls in self.image_urls_batch]

    def test_news_paginator_page_size(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(self.response.data.get("news")), 12)

    def test_news_paginator_links(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        links = self.response.data.get("links")
        self.assertIn("next", links)
        self.assertIn("previous", links)
        self.assertIsNotNone(links.get("next"))
        self.assertIsNone(links.get("previous"))

    def test_news_paginator_page_number(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.data.get("page_number"), 1)
