from django.test import TestCase

from events.models import Events, EventsImageURL
from disciplines.models import Disciplines


class EventsModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.discipline = Disciplines.objects.create(
            name="Тестовая спортивная дисциплина",
            description="Описание спортивной дисциплины"
        )
        cls.event = Events.objects.create(
            name="Тестовое событие",
            description="Обычный текст",
            discipline=cls.discipline
        )

    def test_verbose_name(self):
        field_verboses = {
            "name": "Название события",
            "start_date": "Дата проведения события",
            "image_urls": "Изображения для события",
            "description": "Описание события",
            "place": "Место события",
            "rules": "Правила проведения события",
            "deadline_registration_date": "Дата окончания регистрации на событие",
            "discipline": "Дисциплина для события"
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.event._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        field_help_texts = {
            "name": "Введите название события",
            "image_urls": "Добавьте ссылки на изображения с событиями",
            "description": "Напишите текст о событии до 5000 символов",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.event._meta.get_field(value).help_text, expected
                )


class EventsImageURLModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.discipline = Disciplines.objects.create(
            name="Тестовая спортивная дисциплина",
            description="Описание спортивной дисциплины"
        )
        cls.event = Events.objects.create(
            name="Тестовое событие",
            description="Обычный текст",
            discipline=cls.discipline
        )
        cls.image = EventsImageURL.objects.create(
            events=cls.event,
            image_url="https://clck.ru/3BhzwT",
        )
        cls.event.image_urls.add(cls.image)

    def test_verbose_name(self):
        field_verboses = {
            "events": "Событие",
            "image_url": "Ссылка на изображение события"
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.image._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        field_help_texts = {
            "image_url": "Укажите URL-адрес изображения о событии",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.image._meta.get_field(value).help_text, expected
                )

    def test_image_in_events(self):
        event = Events.objects.get(pk=1)
        image = EventsImageURL.objects.get(pk=1)
        self.assertEqual(image, event.image_urls.all()[0])
