from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import (
    About,
    BannerVideo,
    BrandBook,
    MemberRole,
    OurMembers,
    PartnerLogo,
)


@admin.register(BannerVideo)
class BannerVideoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "video_url",
    )


@admin.register(BrandBook)
class BrandBookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "pub_date",
        "file",
        "is_active",
    )
    list_filter = ("pub_date",
                   "is_active",)
    search_fields = ("name",)


@admin.register(OurMembers)
class OurMembersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "role",
        "name",
        "short_text_preview",
        "image_url",
    )
    list_filter = ("role",)
    search_fields = ("name",
                     "short_text_preview")

    def short_text_preview(self, obj: OurMembers) -> str:
        """
        Генерирует краткий текст новости.
        :param obj: Объект разработчика (экземпляр класса News).
        :type obj: News.

        :return: Краткий текст новости,
        сокращенной до 50 символов.
        :rtype: str.

        """
        return truncatechars(obj.description, 50)

    short_text_preview.short_description = "Краткий текст"


@admin.register(MemberRole)
class MemberRoleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "short_text_preview",
        "image_url",
    )
    search_fields = ("name",
                     "short_text_preview")

    def short_text_preview(self, obj: About) -> str:
        """
        Генерирует краткий текст новости.
        :param obj: Объект разработчика (экземпляр класса News).
        :type obj: News.

        :return: Краткий текст новости,
        сокращенной до 50 символов.
        :rtype: str.

        """
        return truncatechars(obj.description, 50)

    short_text_preview.short_description = "Краткий текст"


@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "image_url",
    )
    search_fields = ("name_role",)
