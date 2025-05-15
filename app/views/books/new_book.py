from django.contrib.auth.decorators import login_required
from ...models import Author, Category, Editorial, Book
from django.shortcuts import render


@login_required
def new_book(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    editorials = Editorial.objects.all()

    context = {
        "authors": authors,
        "categories": categories,
        "editorials": editorials,
    }

    if request.method == "POST":
        title = request.POST.get("title")
        isbn = request.POST.get("isbn")
        author_id = request.POST.get("author")
        editorial_id = request.POST.get("editorial")
        category_id = request.POST.get("category")
        stock = request.POST.get("stock")

        if not all([title, isbn, author_id, editorial_id, category_id, stock]):
            return render(
                request,
                "pages/books/new_book.html",
                context={**context, "error": "All fields is required"},
            )

        if Book.objects.filter(isbn=isbn).exists():
            return render(
                request,
                "pages/books/new_book.html",
                context={**context, "error": "ISBN already exists"},
            )

        new_book = Book.objects.create(
            title=title,
            isbn=isbn,
            author_id=author_id,
            publisher_id=editorial_id,
            category_id=category_id,
            stock=stock,
        )
        new_book.save()

        return render(
            request,
            "pages/books/new_book.html",
            context={**context, "success": "Book created successfully"},
        )

    return render(request, "pages/books/new_book.html", context)
