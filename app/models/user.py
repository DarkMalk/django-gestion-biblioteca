from django.contrib.auth.hashers import make_password
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

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith("pbkdf2_sha256"):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


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
            {"fields": ("username", "email")},
        ),
        (
            "Password",
            {"fields": ("password",), "description": "Raw passwords are not shown."},
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
