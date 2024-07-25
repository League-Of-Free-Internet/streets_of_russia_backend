from disciplines.models import Disciplines, DisciplinesImageURL
from events.models import Events, EventsImageURL
from news.models import News, NewsImageURL


class DisciplinesFactory:
    @staticmethod
    def create_discipline(name, slug, description, rules):
        return Disciplines.objects.create(
            name=name,
            slug=slug,
            description=description,
            rules=rules
        )


class DisciplinesImageURLFactory:
    @staticmethod
    def create_discipline_image_url(discipline, image_url):
        return DisciplinesImageURL.objects.create(
            discipline=discipline,
            image_url=image_url
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


class NewsFactory:
    @staticmethod
    def create_news(name, description):
        return News.objects.create(
            name=name,
            description=description
        )


class NewsImageURLFactory:
    @staticmethod
    def create_news_image_url(news, image_url):
        return NewsImageURL.objects.create(
            news=news,
            image_url=image_url
        )
