from rest_framework import serializers

from events.models import Events, EventsImageURL
from news.models import ImageURL, News
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


class ImageURLSerializer(serializers.ModelSerializer):
    """Сериализатор url-ссылок изображений для новостей."""

    class Meta:
        fields = ("image_url",)
        model = ImageURL


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор новостей."""

    image_urls = ImageURLSerializer(many=True)

    class Meta:
        model = News
        fields = ("id", "name", "description", "image_urls")


class EventsImageURLSerializer(serializers.ModelSerializer):
    """Сериализатор url-ссылок изображений для событий."""

    class Meta:
        model = EventsImageURL
        fields = ("image_url",)


class EventsSerializer(serializers.ModelSerializer):
    """Сериализатор событий."""

    image_urls = EventsImageURLSerializer(many=True)

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
