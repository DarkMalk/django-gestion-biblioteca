from django.contrib.auth.decorators import login_required
from ...models import Book, Category, Author, Editorial
from django.shortcuts import render, redirect


@login_required
def edit_book(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    categories = Category.objects.all()
    authors = Author.objects.all()
    editorials = Editorial.objects.all()

    if not book:
        return redirect("books")

    context = {
        "book": book,
        "categories": categories,
        "authors": authors,
        "editorials": editorials,
    }

    if request.method == "POST":
        title = request.POST.get("title")
        isbn = request.POST.get("isbn")
        author_id = request.POST.get("author")
        category_id = request.POST.get("category")
        editorial_id = request.POST.get("editorial")
        stock = request.POST.get("stock")
        active = request.POST.get("active")

        if not all([title, isbn, author_id, category_id, editorial_id, stock, active]):
            return render(
                request,
                "pages/books/edit_book.html",
                {**context, "error": "All fields are required."},
            )

        try:
            book.title = title
            book.isbn = isbn
            book.author_id = author_id
            book.category_id = category_id
            book.publisher_id = editorial_id
            book.stock = stock
            book.active = active

            book.save()

            return render(
                request,
                "pages/books/edit_book.html",
                {**context, "success": "Book updated successfully."},
            )
        except Exception as e:
            print(e)
            return render(
                request,
                "pages/books/edit_book.html",
                {**context, "error": "Error updating book"},
            )

    return render(request, "pages/books/edit_book.html", context)
