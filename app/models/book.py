from django.contrib import admin
from django.db import models

from .category import Category
from .author import Author
from .editorial import Editorial


class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "isbn",
        "publisher",
        "category",
        "stock",
        "active",
        "created_at",
    )
    search_fields = (
        "title",
        "author__name",
        "isbn",
        "category__name",
    )
    ordering = ("id",)
    list_per_page = 10
