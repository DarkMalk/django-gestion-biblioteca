from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import Book, Loan, User
from datetime import date, timedelta


@login_required
def new_loan(request):
    if request.user.role == "lector":
        return redirect("index")

    min_due_date = date.today() + timedelta(days=1)
    max_due_date = date.today() + timedelta(days=7)

    books = Book.objects.filter(active=True)
    users = User.objects.filter(is_active=True)

    context = {
        "books": books,
        "users": users,
        "today": date.today(),
        "min_due_date": min_due_date,
        "max_due_date": max_due_date,
    }

    if request.method == "POST":
        book_id = request.POST.get("book")
        user_id = request.POST.get("user")
        due_date = request.POST.get("due_date")

        if not all([book_id, user_id, due_date]):
            return render(
                request,
                "pages/loans/new_loan.html",
                {**context, "error": "All fields are required."},
            )

        # Verificar si un usuario ya tiene un prestamo activo
        if Loan.objects.filter(status="active", user_id=user_id).exists():
            return render(
                request,
                "pages/loans/new_loan.html",
                {
                    **context,
                    "error": "User already has an active loan.",
                },
            )

        if Book.objects.get(id=book_id).stock <= 0:
            return render(
                request,
                "pages/loans/new_loan.html",
                {
                    **context,
                    "error": "Book is out of stock.",
                },
            )

        if due_date < str(min_due_date) or due_date > str(max_due_date):
            return render(
                request,
                "pages/loans/new_loan.html",
                {
                    **context,
                    "error": "Due date must be between tomorrow and 7 days from now.",
                },
            )

        try:
            book = Book.objects.get(id=book_id)
            book.stock -= 1

            new_loan = Loan.objects.create(
                book_id=book_id,
                user_id=user_id,
                due_date=due_date,
            )

            book.save()
            new_loan.save()

            return render(
                request,
                "pages/loans/new_loan.html",
                {**context, "success": "Loan created successfully."},
            )

        except Exception as e:
            print(f"Error creating loan: {e}")

            return render(
                request,
                "pages/loans/new_loan.html",
                {**context, "error": "Error creating loan"},
            )

    return render(request, "pages/loans/new_loan.html", context)
