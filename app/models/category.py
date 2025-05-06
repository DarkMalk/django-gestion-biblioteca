from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    list_per_page = 10
