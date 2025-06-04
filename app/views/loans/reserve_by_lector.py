from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.shortcuts import render
from ...models import Book, Loan
from django.db.models import Q


@login_required
def reserve_by_lector(request, book_id):
    book = Book.objects.filter(id=book_id).first()

    today = datetime.today()
    min_due_date = today + timedelta(days=1)
    max_due_date = min_due_date + timedelta(days=7)

    if not book:
        return render(
            request,
            "pages/loans/reserve_by_lector.html",
            {"error": "Book not found."},
        )

    context = {
        "book": book,
        "today": today,
        "min_due_date": min_due_date,
        "max_due_date": max_due_date,
    }

    if book.stock <= 0:
        return render(
            request,
            "pages/loans/reserve_by_lector.html",
            {
                "error": "This book is not available for reservation.",
                "disabled_button": True,
                **context,
            },
        )

    if Loan.objects.filter(
        Q(status="active") | Q(status="overdue"), user=request.user
    ).exists():
        return render(
            request,
            "pages/loans/reserve_by_lector.html",
            {
                "error": "You already have an active or overdue loan.",
                "disabled_button": "True",
                **context,
            },
        )

    if request.method == "POST":
        due_date = request.POST.get("due_date")
        user = request.user

        if not due_date:
            return render(
                request,
                "pages/loans/reserve_by_lector.html",
                {"error": "Due date is required.", **context},
            )

        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return render(
                request,
                "pages/loans/reserve_by_lector.html",
                {"error": "Invalid due date format.", **context},
            )

        if due_date_obj < min_due_date.date() or due_date_obj > max_due_date.date():
            return render(
                request,
                "pages/loans/reserve_by_lector.html",
                {
                    "error": f"Due date must be between {min_due_date.date()} and {max_due_date.date()}.",
                    **context,
                },
            )

        try:
            Loan.objects.create(
                book=book,
                user=user,
                due_date=due_date_obj,
            )

            book.stock -= 1
            book.save()

            return render(
                request,
                "pages/loans/reserve_by_lector.html",
                {
                    "success": "Book reserved successfully.",
                    **context,
                },
            )

        except Exception as e:
            return render(
                request,
                "pages/loans/reserve_by_lector.html",
                {
                    "error": "An error occurred while reserving the book, please try again later",
                    **context,
                },
            )

    return render(request, "pages/loans/reserve_by_lector.html", context)
