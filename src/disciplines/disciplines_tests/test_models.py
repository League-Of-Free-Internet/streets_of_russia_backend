from django.test import TestCase

from disciplines.models import Disciplines, DisciplinesImageURL


class DisciplinesModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.discipline = Disciplines.objects.create(
            name="Тестовая спортивная дисциплина",
            description="Описание спортивной дисциплины",
            rules="Правила спортивной дисциплины"
        )

    def test_verbose_name(self):
        field_verboses = {
            "name": "Спортивная дисциплина",
            "description": "Описание дисциплины",
            "image_urls": "Изображения для дисциплин",
            "rules": "Правила спортивной дисциплины"
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.discipline._meta.get_field(value).verbose_name,
                    expected
                )

    def test_help_text(self):
        field_help_texts = {
            "name": "Напишите название дисциплины",
            "image_urls": "Добавьте ссылки на изображения с дисциплиной",
            "description": "Напишите описание дисциплины до 5000 символов",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.discipline._meta.get_field(value).help_text, expected
                )


class DisciplinesImageURLModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.discipline = Disciplines.objects.create(
            name="Тестовая спортивная дисциплина",
            description="Описание спортивной дисциплины",
            rules="Правила спортивной дисциплины"
        )
        cls.image = DisciplinesImageURL.objects.create(
            name=cls.discipline,
            image_url="https://clck.ru/3AjpaT",
        )
        cls.discipline.image_urls.add(cls.image)

    def test_verbose_name(self):
        field_verboses = {
            "name": "Спортивная дисциплина",
            "image_url": "Ссылка на изображение с дисциплиной",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.image._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        field_help_texts = {
            "image_url": (
                "Укажите URL-адрес изображения со спортивной дисциплиной"
            ),
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.image._meta.get_field(value).help_text, expected
                )

    def test_image_in_disciplines(self):
        news = Disciplines.objects.get(pk=1)
        image = DisciplinesImageURL.objects.get(pk=1)
        self.assertEqual(image, news.image_urls.all()[0])
