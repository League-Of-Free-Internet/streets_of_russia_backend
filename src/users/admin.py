from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели Пользователя.
    """
    list_display = (
        "id",
        "email",
        "get_full_name",
        # "phone_number",
        "is_active",
        "is_staff",
    )
    list_filter = ("is_active",
                   "is_staff",)
    search_fields = ("get_full_name",
                     # "phone_number",
                     "email")
    CustomUser.get_full_name.short_description = "Имя и Фамилия"
