from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models import UserRole

User = get_user_model()


class CustomUserAPITest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("users-list")
        cls.api_client = APIClient()
        cls.role_1 = UserRole.objects.create(
            name_role="Участник",
            is_active=True,
        )
        cls.role_2 = UserRole.objects.create(
            name_role="Тестовый",
            is_active=False,
        )
        cls.unique_user = {
            "first_name": "Петр",
            "last_name": "Петрович",
            "password1": "qwerty12345",
            "password2": "qwerty12345",
            "email": "pert.pertrovich@test.ru",
            "phone_number": "+79095512366",
            "role": cls.role_1.id
        }

        cls.user_data = {
            "first_name": "Иван",
            "last_name": "Иванов",
            "password1": "qwerty123",
            "password2": "qwerty123",
            "email": "ivan.ivanov@test.ru",
            "phone_number": "+79095512365",
            "role": cls.role_1.id
        }

    def test_post_user(self):
        response = self.api_client.post(
            self.url, self.user_data)
        in_db_user = User.objects.get()
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(
            in_db_user.first_name,
            self.user_data["first_name"])
        self.assertEqual(
            in_db_user.email,
            self.user_data["email"]
        )
        self.assertEqual(
            in_db_user.email,
            self.user_data["email"]
        )
        self.assertEqual(
            in_db_user.phone_number,
            self.user_data["phone_number"]
        )

    def test_create_user_with_mismatched_passwords(self):
        mismatched_data = self.user_data.copy()
        mismatched_data["password2"] = "another123"
        response = self.api_client.post(self.url, mismatched_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_create_user_with_invalid_email(self):
        invalid_email_data = self.user_data.copy()
        invalid_email_data["email"] = "это почта"
        response = self.api_client.post(self.url, invalid_email_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_create_user_with_invalid_phone(self):
        invalid_phone_data = self.user_data.copy()
        invalid_phone_data["phone_number"] = "1315646546"
        response = self.api_client.post(self.url, invalid_phone_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_unique_user_phone_number(self):
        response = self.api_client.post(
            self.url, self.unique_user)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)
        not_unique_phone = self.user_data.copy()
        not_unique_phone["phone_number"] = "+79095512366"
        failed_response = self.api_client.post(
            self.url, not_unique_phone)
        self.assertEqual(
            failed_response.status_code,
            status.HTTP_400_BAD_REQUEST)

    def test_unique_user_email(self):
        response = self.api_client.post(
            self.url, self.unique_user)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)
        not_unique_email = self.user_data.copy()
        not_unique_email["email"] = "pert.pertrovich@test.ru"
        failed_response = self.api_client.post(
            self.url, not_unique_email)
        self.assertEqual(
            failed_response.status_code,
            status.HTTP_400_BAD_REQUEST)
