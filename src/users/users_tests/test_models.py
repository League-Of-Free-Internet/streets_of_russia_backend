from django.contrib.auth import get_user_model
from django.test import TestCase
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManagerTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.User = get_user_model()
        cls.user = cls.User.objects.create_user(
            email="user@example.ru",
            password="Fool123",
            first_name="Normal",
            last_name="User",
            phone_number="+79999999999")
        cls.admin_user = cls.User.objects.create_superuser(
            email="admin@example.ru",
            password="adminpass123",
            first_name="Admin",
            last_name="User",
            phone_number="+79999999998"
        )
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()
        cls.admin_user.delete()

    def test_create_user(self):
        self.assertEqual(self.user.email, "user@example.ru")
        self.assertTrue(self.user.check_password("Fool123"))
        self.assertEqual(self.user.first_name, "Normal")
        self.assertEqual(self.user.last_name, "User")
        self.assertEqual(self.user.phone_number, "+79999999999")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError) as context:
            self.User.objects.create_user(email="", password="foo")
        self.assertEqual(str(context.exception), "The Email field must be set")

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.email, "admin@example.ru")
        self.assertTrue(self.admin_user.check_password("adminpass123"))
        self.assertEqual(self.admin_user.first_name, "Admin")
        self.assertEqual(self.admin_user.last_name, "User")
        self.assertEqual(self.admin_user.phone_number, "+79999999998")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)

    def test_create_superuser_without_email(self):
        with self.assertRaises(ValueError) as context:
            self.User.objects.create_superuser(email="", password="foo")
        self.assertEqual(str(context.exception), "The Email field must be set")

    def test_user_verbose_name(self):
        user = CustomUserManagerTests.user
        field_verboses = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "phone_number": "Номер телефона",
            "email": "email",
            "role": "Роль",
            "is_active": "Аккаунт активен",
            "is_staff": "Является персоналом",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    user._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        user = CustomUserManagerTests.user
        field_help_texts = {
            "first_name": "Введите имя",
            "last_name": "Введите фамилию",
            "phone_number": "Введите номер телефона в формате +7999 999 99 99",
            "role": "Название роли, к которой относится пользователь",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    user._meta.get_field(value).help_text, expected
                )
