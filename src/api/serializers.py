from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import (
    CommonPasswordValidator,
    MinimumLengthValidator,
    NumericPasswordValidator,
    UserAttributeSimilarityValidator,
)
from phonenumber_field.serializerfields import (
    PhoneNumberField as SerializerPhoneNumberField,
)
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)

from core.constants import FORMAT_DATE
from core.utils import get_image_urls
from disciplines.models import Disciplines
from events.models import EventRegistration, Events, EventsImageURL
from news.models import News
from users.models import CustomUser, UserRole

User = get_user_model()


class UserSerializer(serializers.Serializer):
    """Сериализатор пользователей."""

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    phone_number = SerializerPhoneNumberField()
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
        email = data.get("email")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Пользователь с таким адресом "
                + "электронной почты уже существует.")
        phone_number = data.get("phone_number")
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError(
                "Пользователь с таким номером "
                + "телефона уже существует.")
        return data

    def validate_first_name(self, field: str):
        if field.isalpha():
            return field
        raise serializers.ValidationError("Имя должно содержать только буквы.")

    def validate_last_name(self, field: str):
        if field.isalpha():
            return field
        raise serializers.ValidationError("Имя должно содержать только буквы.")

    def validate_password1(self, value):
        user = self.instance
        if user is None:
            user = User(email=self.initial_data.get("email"))

        validators = [
            UserAttributeSimilarityValidator(),
            MinimumLengthValidator(),
            CommonPasswordValidator(),
            NumericPasswordValidator(),
        ]

        errors = []
        for validator in validators:
            try:
                validator.validate(value, user)
            except serializers.ValidationError as error:
                errors.extend(error.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return value

    def create(self, validated_data):
        validated_data.pop("password2")
        return CustomUser.objects.create_user(
            password=make_password(validated_data.pop("password1")),
            **validated_data
        )


class ProjectTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class ProjectTokenRefreshSerializer(TokenRefreshSerializer):
    pass


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор новостей."""

    image_urls = serializers.SerializerMethodField()
    pub_date = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id",
            "name",
            "image_urls",
            "description",
            "pub_date"
        )

    @staticmethod
    def get_image_urls(obj):
        return get_image_urls(obj)

    @staticmethod
    def get_pub_date(obj):
        """Форматирование даты в формат: `2024-07-14 11:57:06`"""
        return obj.pub_date.strftime(FORMAT_DATE)

    def to_representation(self, instance):
        """Если запрос на получение одной новости,
        то `pub_date` включается в ответ. В иных случаях
        `pub_date` исключается из ответа"""
        result = super().to_representation(instance)
        request = self.context.get("request")
        if request and request.resolver_match.url_name == "news-detail":
            return result
        result.pop("pub_date", None)
        return result


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


class EventRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и удаления регистрации пользователя
     на конкретное событие."""

    class Meta:
        model = EventRegistration
        fields = "__all__"
        read_only_fields = ("id", "user", "event", "registration_date")


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
