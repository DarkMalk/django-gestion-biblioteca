from django.contrib.auth.models import AbstractUser
from django.contrib.admin import ModelAdmin
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("librarian", "Librarian"),
        ("lector", "Lector"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="lector")


class UserAdmin(ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
        "is_staff",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff", "role")
    ordering = ("username",)
    fieldsets = (
        (
            None,
            {"fields": ("username", "password")},
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "role")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    readonly_fields = ("password",)
