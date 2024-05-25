from rest_framework import serializers

from news.models import News, NewsImageURL
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей.
    """

    class Meta:
        fields = "__all__"
        model = CustomUser


class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("image_url", )
        model = NewsImageURL


class NewsSerializer(serializers.ModelSerializer):
    image_urls = ImageURLSerializer(many=True)

    class Meta:
        model = News
        fields = ("id", "name", "description", "image_urls")
