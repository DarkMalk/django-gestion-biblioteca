from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models
from ..models import Book


class Loan(models.Model):
    STATUS_CHOICES = [
        ("returned", "Returned"),
        ("overdue", "Overdue"),
        ("active", "Active"),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        default=STATUS_CHOICES[2][0],
        max_length=8,
        choices=STATUS_CHOICES,
    )


class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "request_date", "due_date", "return_date", "status")
    list_filter = ("status",)
    search_fields = ("book__title", "user__username")
    ordering = ("-request_date",)
