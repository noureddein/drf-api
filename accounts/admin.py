from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "first_name",
                    "last_name", "phone_number", "user_type"]

    fieldsets = UserAdmin.fieldsets + (
        ("User Info",
         {
             "fields": ["phone_number", "user_type", ]
         }),
    )
