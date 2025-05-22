from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..models import Book, Loan, User
from datetime import datetime, timedelta
from ..utils import (
    books_per_category,
    new_members_last_seven_months as new_members_utils,
    library_activity_last_seven_months as library_activity_utils,
)


@login_required
def dashboard(request):
    if request.user.role == "lector":
        # Redirect a la pagina de todos los libros (pagina principal para lectores)
        return redirect("index")

    books = Book.objects.all()
    users = User.objects.all()
    loans = Loan.objects.all()

    # Obtener los últimos 7 meses (incluyendo el mes actual)
    today = datetime.today().replace(day=1)
    months = [(today - timedelta(days=30 * i)).replace(day=1) for i in range(6, -1, -1)]
    month_labels = [
        {"month": {"name": m.strftime("%b"), "id": m.month}, "year": m.year}
        for m in months
    ]

    total_books = books.count()
    total_users = users.count()
    active_loans = loans.filter(status="active").count()
    overdue_loans = loans.filter(status="overdue").count()
    books_by_category = books_per_category(books)
    new_members_last_seven_months = new_members_utils(month_labels, users)
    library_activity_last_seven_months = library_activity_utils(month_labels, loans)

    data = {
        "total_books": total_books,
        "books_by_category": books_by_category,
        "total_members": total_users,
        "active_loans": active_loans,
        "overdue_loans": overdue_loans,
        "new_members_last_seven_months": new_members_last_seven_months,
        "library_activity_last_seven_months": library_activity_last_seven_months,
    }

    return render(request, "pages/dashboard.html", context=data)
