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
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        [news.delete() for news in self.news_batch]
        [image_urls.delete() for image_urls in self.image_urls_batch]

    def test_news_paginator_page_size(self):
        self.assertEqual(len(self.response.data.get("news")), 12)

    def test_news_paginator_links(self):
        links = self.response.data.get("links")
        self.assertIn("next", links)
        self.assertIn("previous", links)
        self.assertIsNotNone(links.get("next"))
        self.assertIsNone(links.get("previous"))

    def test_news_paginator_page_number(self):
        self.assertEqual(self.response.data.get("page_number"), 1)

    def test_news_paginator_invalid_page(self):
        self.assertEqual(
            self.client.get(reverse("news-list") + "?page=1000").status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_news_paginator_total_count(self):
        self.assertEqual(self.response.data.get("count"), 100)

    def test_news_paginator_page_links(self):
        response = self.client.get(self.response.data.get("links").get("next"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get("links").get("previous"))
        self.assertEqual(response.data.get("page_number"), 2)

    def test_news_paginator_last_page(self):
        response = self.client.get(reverse("news-list") + "?page=9")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("news")), 4)
        self.assertIsNone(response.data.get("links").get("next"))
        self.assertIsNotNone(response.data.get("links").get("previous"))
