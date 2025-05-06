from django.urls import path
from .views import index, books, loans, login, register, logout

urlpatterns = [
    path("dashboard", index, name="dashboard"),
    path("books", books, name="books"),
    path("", books, name="index"),
    path("loans", loans, name="loans"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
]
