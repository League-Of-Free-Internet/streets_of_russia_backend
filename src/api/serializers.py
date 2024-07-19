from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.utils import get_image_urls
from disciplines.models import Disciplines
from events.models import Events, EventSignUp, EventsImageURL
from news.models import News
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

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        return CustomUser.objects.create_user(
            password=make_password(validated_data.pop("password1")),
            **validated_data
        )


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор новостей."""

    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = News
        exclude = ("pub_date",)

    @staticmethod
    def get_image_urls(obj):
        return get_image_urls(obj)


class EventsImageURLSerializer(serializers.PrimaryKeyRelatedField,
                               serializers.ModelSerializer):
    """Сериализатор url-ссылок изображений для событий."""

    class Meta:
        model = EventsImageURL
        fields = ("image_url",)


class FourLatestEventsSerializer(serializers.ModelSerializer):
    """Сериализатор для последних 4 событий."""

    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Events
        exclude = (
            "deadline_registration_date",
            "discipline",
            "rules"
        )

    @staticmethod
    def get_image_urls(obj):
        return get_image_urls(obj)


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для конкретного события."""

    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Events
        exclude = ("discipline",)

    @staticmethod
    def get_image_urls(obj):
        return get_image_urls(obj)


class EventSignUpSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя на конкретное событие."""

    class Meta:
        model = EventSignUp
        fields = "__all__"
        read_only_fields = ("user", "event", "registration_date")


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
        exclude = ("id", "name")

    @staticmethod
    def get_image_urls(obj):
        return get_image_urls(obj)
