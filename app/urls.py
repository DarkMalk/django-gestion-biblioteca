from django.urls import path
from .views import index, books

urlpatterns = [
    path("dashboard", index, name="dashboard"),
    path("books", books, name="books"),
]
