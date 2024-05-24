from rest_framework import serializers

from users.models import CustomUser
from news.models import News, ImageURL


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей"""
    class Meta:
        fields = "__all__"
        model = CustomUser


class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("image_url", )
        model = ImageURL


class NewsSerializer(serializers.ModelSerializer):
    image_urls = ImageURLSerializer(many=True)

    class Meta:
        model = News
        fields = ("id", "name", "description", "image_urls")
