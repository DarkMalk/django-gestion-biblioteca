from django.db import models
from django.contrib import admin
from datetime import datetime


class Author(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    list_per_page = 10
