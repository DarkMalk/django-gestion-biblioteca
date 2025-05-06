from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Book, Category


def books(request):
    category = request.GET.get("category")
    categories = Category.objects.values_list("name", flat=True)

    books = Book.objects.all()

    if category in categories:
        books = books.filter(category__name=category)

    paginator = Paginator(books, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "pages/books.html", context={"books": page_obj})
