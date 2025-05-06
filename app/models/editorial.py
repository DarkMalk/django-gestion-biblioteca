from django.db import models
from django.contrib import admin


class Editorial(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return self.name


class EditorialAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "email")
    search_fields = ("name",)
    ordering = ("id",)
    list_per_page = 10
