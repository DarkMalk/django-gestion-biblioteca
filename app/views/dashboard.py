from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..models import Book, Loan, User
from django.db.models.functions import TruncMonth
from django.db.models import Count


@login_required
def dashboard(request):
    if request.user.role == "lector":
        # Redirect a la pagina de todos los libros (pagina principal para lectores)
        return redirect("index")

    books = Book.objects.all()

    users_by_month = (
        User.objects.annotate(month=TruncMonth("date_joined"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("month")
    )

    users_by_month_data = {
        entry["month"].strftime("%b"): entry["count"] for entry in users_by_month
    }

    total_books = books.count()
    total_users = User.objects.count()
    active_loans = Loan.objects.filter(status="active").count()
    overdue_loans = Loan.objects.filter(status="overdue").count()
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
        "total_members": total_users,
        "active_loans": active_loans,
        "overdue_loans": overdue_loans,
        "new_members_last_seven_months": users_by_month_data,
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
