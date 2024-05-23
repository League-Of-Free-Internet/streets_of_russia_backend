from django.contrib import admin

from .models import CustomUser, UserRole


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
        "phone_number",
        "role",
        "is_active",
        "is_staff",
    )
    list_filter = ("is_active",
                   "is_staff",
                   "role",)
    search_fields = ("get_full_name",
                     "phone_number",
                     "email")
    CustomUser.get_full_name.short_description = "Имя и Фамилия"


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_role",
        "is_active",
    )
    search_fields = ("name_role",)
    list_filter = ("is_active",)
