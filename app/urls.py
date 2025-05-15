from django.urls import path
from .views import (
    index,
    books,
    loans,
    login,
    register,
    logout,
    members,
    new_book,
    new_loan,
)

urlpatterns = [
    path("dashboard", index, name="dashboard"),
    path("books", books, name="books"),
    path("books/new", new_book, name="new_book"),
    path("", books, name="index"),
    path("loans", loans, name="loans"),
    path("loans/new", new_loan, name="new_loan"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
    path("members", members, name="members"),
]
