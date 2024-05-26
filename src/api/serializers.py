from rest_framework import serializers

from disciplines.models import Disciplines
from events.models import Events, EventsImageURL
from news.models import News, NewsImageURL
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""

    class Meta:
        fields = "__all__"
        model = CustomUser
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


# class NewsImageURLSerializer(serializers.ModelSerializer):
#     """Сериализатор url-ссылок изображений для новостей."""
#
#     class Meta:
#         fields = ("image_url",)
#         model = NewsImageURL


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор новостей."""

    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ("id", "name", "description", "image_urls")

    @staticmethod
    def get_image_urls(obj):
        image_urls = NewsImageURL.objects.all()
        return [url.image_url for url in image_urls]



class EventsImageURLSerializer(serializers.PrimaryKeyRelatedField,
                               serializers.ModelSerializer):
    """Сериализатор url-ссылок изображений для событий."""

    class Meta:
        model = EventsImageURL
        fields = ("image_url",)


class EventsSerializer(serializers.ModelSerializer):
    """Сериализатор событий."""

    image_urls = EventsImageURLSerializer(
        many=True, queryset=EventsImageURL.objects.all())

    class Meta:
        model = Events
        fields = (
            "id",
            "name",
            "description",
            "image_urls",
            "start_date",
            "place",
            "rules",
            "deadline_registration_date"
        )


class DisciplinesNamesListSerializer(serializers.Serializer):
    """Сериализатор для вывода списка названий спортивных дисциплин."""

    names = serializers.SerializerMethodField()

    @staticmethod
    def get_names(obj: Disciplines) -> list[str]:
        disciplines = Disciplines.objects.all()
        return [discipline.name for discipline in disciplines]


class ShortDisciplinesSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода краткого содержания спортивных дисциплин."""

    class Meta:
        model = Disciplines
        fields = (
            "image_urls",
            "description"
        )


class FullDisciplinesSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода полного содержания спортивных дисциплин."""

    class Meta:
        model = Disciplines
        fields = (
            "image_urls",
            "description",
            "rules"
        )
