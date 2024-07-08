from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.utils import get_image_urls
from disciplines.models import Disciplines, DisciplinesImageURL
from events.models import Events, EventsImageURL
from news.models import News, NewsImageURL
from users.models import CustomUser, UserRole


class UserSerializer(serializers.Serializer):
    """Сериализатор пользователей."""

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    role = serializers.PrimaryKeyRelatedField(
        queryset=UserRole.objects.all(),
        many=False
    )

    class Meta:
        fields = (
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
            "phone_number",
            "role",
        )
        model = CustomUser

    @staticmethod
    def validate_passwords(attrs):
        password_1 = attrs.get("password1")
        password_2 = attrs.pop("password2")
        if password_1 != password_2:
            raise serializers.ValidationError("Пароли не совпадают.")
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            password=make_password(validated_data.pop("password1")),
            **validated_data
        )


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

    names = serializers.ListField(child=serializers.CharField())


class DisciplinesShortSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода краткого содержания спортивных дисциплин."""

    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Disciplines
        fields = (
            "image_urls",
            "description"
        )

    @staticmethod
    def get_image_urls(obj):
        return get_image_urls(obj)


class DisciplinesFullSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода полного содержания спортивных дисциплин."""

    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Disciplines
        exclude = ["id", "name"]

    @staticmethod
    def get_image_urls(obj):
        return get_image_urls(obj)
