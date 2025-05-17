from django.shortcuts import render, redirect
from ...models import Book


def view_book(request, book_id):
    book = Book.objects.filter(id=book_id, active=True).first()

    if not book:
        return redirect("books")

    context = {"book": book}

    return render(request, "pages/books/view_book.html", context)
