from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from api.api_tests.factories import (
    DisciplinesFactory,
    EventsFactory,
    EventsImageURLFactory,
)
from events.models import EventRegistration
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
            slug="test-discipline",
            description="Описание спортивной дисциплины",
            rules="Правила тестовой спортивной дисциплины"
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
        response = self.client.get(reverse("latest-events-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.data["count"], 2)
        self.assertIn("events", response.data)
        events = response.data["events"]
        events_names = {event["name"] for event in events}
        event_images_urls = {image_url for event in events for image_url in
                             event["image_urls"]}
        self.assertIn(self.event_1.name, events_names)
        self.assertIn(self.event_2.name, events_names)
        self.assertIn(self.image_1.image_url, event_images_urls)
        self.assertIn(self.image_2.image_url, event_images_urls)
        self.assertIn(self.image_3.image_url, event_images_urls)

    def test_get_event(self):
        response = self.client.get(reverse(
            "event-detail", args=[self.event_1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.event_1.name)
        self.assertEqual(
            response.data["description"], self.event_1.description
        )
        self.assertIn(self.image_1.image_url, response.data["image_urls"])
        self.assertNotIn(self.image_2.image_url, response.data["image_urls"])
        self.assertNotIn(self.image_3.image_url, response.data["image_urls"])

    def test_successful_signup(self):
        response = self.client.post(reverse(
            "event-sign-up-list", args=[self.event_1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            EventRegistration.objects.filter(
                user=self.user, event=self.event_1).exists()
        )

    def test_duplicate_signup(self):
        EventRegistration.objects.create(user=self.user, event=self.event_1)
        response = self.client.post(
            reverse("event-sign-up-list", args=[self.event_1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_successful_signout(self):
        EventRegistration.objects.create(user=self.user, event=self.event_1)
        response = self.client.delete(reverse(
            "event-sign-out-detail", args=[self.event_1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            EventRegistration.objects.filter(
                user=self.user, event=self.event_1).exists()
        )

    def test_non_empy_data(self):
        response = self.client.post(
            reverse(
                "event-sign-up-list",
                args=[self.event_1.id]
            ),
            data={"some_field": "some_value"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nonexistent_event(self):
        response = self.client.post(reverse(
            'event-sign-up-list', args=[999])
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_missing_event_id(self):
        with self.assertRaises(NoReverseMatch):
            self.client.post(
                reverse('event-sign-up-list', args=[None])
            )

    def test_unauthenticated_user(self):
        self.client.credentials()
        response = self.client.post(reverse(
            "event-sign-up-list", args=[self.event_1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
