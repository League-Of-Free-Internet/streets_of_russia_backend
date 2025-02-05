from django.test import TestCase

from news.models import News, NewsImageURL

PK = 1


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
            "pub_date": "Дата публикации новости",
            "image_urls": "Добавьте ссылки на изображения",
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


class NewsImageURLModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.news = News.objects.create(
            name="Тестовая Новость",
            description="Обычный текст",
        )
        cls.image = NewsImageURL.objects.create(
            news=cls.news,
            image_url="https://clck.ru/3AjpaT",
        )
        cls.news.image_urls.add(cls.image)

    def test_verbose_name(self):
        image = NewsImageURLModelTest.image
        field_verboses = {
            "news": "Новость",
            "image_url": "Ссылка на изображение для новости",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    image._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        image = NewsImageURLModelTest.image
        field_help_texts = {
            "news": "",
            "image_url": "Укажите URL-адрес изображения о новости",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    image._meta.get_field(value).help_text, expected
                )

    def test_image_in_news(self):
        """
        Тест проверяет, что изображение присутствует
        в списке изображений новости.
        """
        try:
            news = News.objects.get(pk=PK)
            image = NewsImageURL.objects.get(pk=PK)
        except News.DoesNotExist:
            self.fail(f"News object with pk={PK} does not exist")
        except NewsImageURL.DoesNotExist:
            self.fail(f"NewsImageURL object with pk={PK} does not exist")

        self.assertIn(image, news.image_urls.all(),
                      "Image is not in the list of news images")
