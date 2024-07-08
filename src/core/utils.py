from disciplines.models import DisciplinesImageURL


def get_image_urls(obj):
    image_urls = DisciplinesImageURL.objects.filter(name=obj.id)
    return [url.image_url for url in image_urls]
