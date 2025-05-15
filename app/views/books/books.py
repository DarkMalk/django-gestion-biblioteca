from django.core.paginator import Paginator
from django.shortcuts import render
from ...models import Book, Category


def books(request):
    search = request.GET.get("search")
    category = request.GET.get("category")
    categories = Category.objects.values_list("name", flat=True)

    books = Book.objects.all()

    if category in categories:
        books = books.filter(category__name=category)

    if search:
        books = books.filter(title__icontains=search)

    paginator = Paginator(books, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "pages/books/books.html",
        context={"books": page_obj, "categories": categories},
    )
