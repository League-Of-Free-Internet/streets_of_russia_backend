from django.test import TestCase

from ..models import ImageURL, News


class NewsModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.news = News.objects.create(
            name="Тестовая Новость",
            description="Обычный текст",
        )

    def test_verbose_name(self):
        news = NewsModelTest.news
        field_verboses = {
            "name": "Название новости",
            "pub_date": "Дата",
            "image_urls": "Изображения",
            "description": "Содержание новости",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    news._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        news = NewsModelTest.news
        field_help_texts = {
            "name": "Введите название новости",
            "image_urls": "Добавьте ссылки на изображения",
            "description": "Напишите текст новости до 5000 символов",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    news._meta.get_field(value).help_text, expected
                )


class ImageURLModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.news = News.objects.create(
            name="Тестовая Новость",
            description="Обычный текст",
        )
        cls.image = ImageURL.objects.create(
            news=cls.news,
            image_url="https://clck.ru/3AjpaT",
        )
        cls.news.image_urls.add(cls.image)

    def test_verbose_name(self):
        image = ImageURLModelTest.image
        field_verboses = {
            "news": "Новость",
            "image_url": "Ссылка на изображение",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    image._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        image = ImageURLModelTest.image
        field_help_texts = {
            "news": "",
            "image_url": "Укажите URL-адрес изображения",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    image._meta.get_field(value).help_text, expected
                )

    def test_image_in_news(self):
        news = News.objects.get(pk=1)
        image = ImageURL.objects.get(pk=1)
        self.assertEqual(image, news.image_urls.all()[0])
