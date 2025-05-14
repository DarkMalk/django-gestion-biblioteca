from django.db import models
from django.contrib import admin


class Editorial(models.Model):
    name = models.CharField(max_length=80, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EditorialAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "email", "created_at")
    search_fields = ("name",)
    ordering = ("id",)
    list_per_page = 10
