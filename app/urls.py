from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard", index, name="dashboard"),
    path("books", books, name="books"),
    path("books/new", new_book, name="new_book"),
    path("books/<int:book_id>", view_book, name="view_book"),
    path("books/<int:book_id>/edit", edit_book, name="edit_book"),
    path("", books, name="index"),
    path("loans", loans, name="loans"),
    path("loans/new", new_loan, name="new_loan"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
    path("members", members, name="members"),
    path("members/<int:member_id>", view_member, name="view_member"),
    path("members/<int:member_id>/edit", edit_member, name="edit_member"),
    path("members/new", new_member, name="new_member"),
]
