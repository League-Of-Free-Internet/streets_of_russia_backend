from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from api.api_tests.factories import (
    DisciplinesFactory,
    EventsFactory,
    EventsImageURLFactory,
)
from users.models import CustomUser


class EventsAPITest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
            email="admin@test.com",
            password="admin_password"
        )
        self.access_token = str(AccessToken.for_user(self.user))
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.discipline = DisciplinesFactory.create_discipline(
            name="Тестовая спортивная дисциплина",
            description="Описание спортивной дисциплины"
        )
        self.event_1 = EventsFactory.create_event(
            name="Тестовое событие 1",
            description="Описание тестового события 1",
            discipline=self.discipline
        )
        self.event_2 = EventsFactory.create_event(
            name="Тестовое событие 2",
            description="Описание тестового события 2",
            discipline=self.discipline
        )
        self.image_1 = EventsImageURLFactory.create_event_image_url(
            self.event_1, "https://clck.ru/3C3AMn"
        )
        self.image_2 = EventsImageURLFactory.create_event_image_url(
            self.event_2, "https://clck.ru/3C3AQR"
        )
        self.image_3 = EventsImageURLFactory.create_event_image_url(
            self.event_2, "https://clck.ru/3C3AUu"
        )

    def tearDown(self):
        self.image_1.delete()
        self.image_2.delete()
        self.image_3.delete()
        self.event_1.delete()
        self.event_2.delete()
        self.discipline.delete()
        self.user.delete()

    def test_get_all_events(self):
        url = reverse("latest-events-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.data["count"], 2)
        self.assertIn("events", response.data)
        events = response.data["events"]
        events_names = {event["name"] for event in events}
        event_image_urls = {image_url for event in events for image_url in
                            event["image_urls"]}
        self.assertIn(self.event_1.name, events_names)
        self.assertIn(self.event_2.name, events_names)
        self.assertIn(self.image_1.image_url, event_image_urls)
        self.assertIn(self.image_2.image_url, event_image_urls)
        self.assertIn(self.image_3.image_url, event_image_urls)
