from disciplines.models import Disciplines
from events.models import Events, EventsImageURL


class DisciplinesFactory:
    @staticmethod
    def create_discipline(name, description):
        return Disciplines.objects.create(
            name=name,
            description=description
        )


class EventsFactory:
    @staticmethod
    def create_event(name, description, discipline):
        return Events.objects.create(
            name=name,
            description=description,
            discipline=discipline
        )


class EventsImageURLFactory:
    @staticmethod
    def create_event_image_url(event, image_url):
        return EventsImageURL.objects.create(
            event=event,
            image_url=image_url
        )
