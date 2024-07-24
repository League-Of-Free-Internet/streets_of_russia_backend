from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from api.api_tests.factories import (
    DisciplinesFactory,
    DisciplinesImageURLFactory,
)
from users.models import CustomUser


class DisciplineAPITest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
            email="admin@test.com",
            password="admin_password"
        )
        self.access_token = str(AccessToken.for_user(self.user))
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.discipline_1 = DisciplinesFactory.create_discipline(
            name="Тестовая спортивная дисциплина 1",
            description="Описание тестовой дисциплины 1",
            rules="Правила тестовой спортивной дисциплины 1"
        )
        self.discipline_2 = DisciplinesFactory.create_discipline(
            name="Тестовая спортивная дисциплина 2",
            description="Описание тестовой дисциплины 2",
            rules="Правила тестовой спортивной дисциплины 2"
        )
        self.image_1 = DisciplinesImageURLFactory.create_discipline_image_url(
            self.discipline_1, "https://clck.ru/3C3AMn"
        )
        self.image_2 = DisciplinesImageURLFactory.create_discipline_image_url(
            self.discipline_2, "https://clck.ru/3C3AQR"
        )
        self.image_3 = DisciplinesImageURLFactory.create_discipline_image_url(
            self.discipline_2, "https://clck.ru/3C3AUu"
        )

    def tearDown(self):
        self.image_1.delete()
        self.image_2.delete()
        self.image_3.delete()
        self.discipline_1.delete()
        self.discipline_2.delete()
        self.user.delete()

    def test_get_all_disciplines_names(self):
        response = self.client.get(reverse("disciplines-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(len(response.data["names"]), 2)
        self.assertIn("names", response.data)
        disciplines_names = {name for name in response.data["names"]}
        self.assertIn(self.discipline_1.name, disciplines_names)
        self.assertIn(self.discipline_2.name, disciplines_names)

    def test_get_discipline_with_short_info(self):
        response = self.client.get(reverse(
            "discipline-short-detail", args=[self.discipline_1.name])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["description"], self.discipline_1.description
        )
        self.assertIn(self.image_1.image_url, response.data["image_urls"])
        self.assertNotIn(self.image_2.image_url, response.data["image_urls"])
        self.assertNotIn(self.image_3.image_url, response.data["image_urls"])

    def test_get_discipline_with_full_info(self):
        response = self.client.get(reverse(
            "discipline-full-detail", args=[self.discipline_1.name])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["description"], self.discipline_1.description
        )
        self.assertEqual(
            response.data["rules"], self.discipline_1.rules
        )
        self.assertIn(self.image_1.image_url, response.data["image_urls"])
        self.assertNotIn(self.image_2.image_url, response.data["image_urls"])
        self.assertNotIn(self.image_3.image_url, response.data["image_urls"])
