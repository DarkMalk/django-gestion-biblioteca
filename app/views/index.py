from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Book


@login_required
def index(request):
    books = Book.objects.all()

    total_books = books.count()
    books_by_category = {}

    for book in books:
        category = book.category.name
        if category in books_by_category:
            books_by_category[category] += 1
        else:
            books_by_category[category] = 1

    data = {
        "total_books": total_books,
        "books_by_category": books_by_category,
        "total_members": 573,
        "active_loans": 145,
        "overdue_loans": 12,
        "new_members_last_seven_months": {
            "Jan": 12,
            "Feb": 15,
            "Mar": 32,
            "Apr": 18,
            "May": 14,
            "Jun": 11,
            "Jul": 9,
        },
        "library_activity_last_seven_months": {
            "Jan": {"loans": 65, "returned": 42},
            "Feb": {"loans": 59, "returned": 55},
            "Mar": {"loans": 80, "returned": 70},
            "Apr": {"loans": 81, "returned": 60},
            "May": {"loans": 56, "returned": 45},
            "Jun": {"loans": 55, "returned": 58},
            "Jul": {"loans": 40, "returned": 45},
        },
    }

    return render(request, "pages/index.html", context=data)
