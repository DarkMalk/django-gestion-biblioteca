from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import Loan, Book, User
from datetime import datetime, timedelta


@login_required
def edit_loan(request, loan_id):
    if request.user.role == "lector":
        return redirect("loans")

    books = Book.objects.filter(active=True)
    users = User.objects.filter(is_active=True)
    loan = Loan.objects.filter(id=loan_id).first()

    today = datetime.today().date()

    max_due_date = today + timedelta(days=14)

    if not loan:
        return redirect("loans")

    context = {
        "loan": loan,
        "books": books,
        "users": users,
        "today": today,
        "max_due_date": max_due_date,
    }

    if request.method == "POST":
        book_id = request.POST.get("book")
        user_id = request.POST.get("user")
        due_date = request.POST.get("due_date")
        return_date = request.POST.get("return_date")

        if not all([book_id, user_id, due_date]):
            return render(
                request,
                "pages/loans/edit_loan.html",
                {**context, "error": "All fields are required"},
            )

        try:
            book_selected = Book.objects.filter(id=book_id).first()
            if not book_selected:
                return render(
                    request,
                    "pages/loans/edit_loan.html",
                    {**context, "error": "Book not found."},
                )

            if book_selected.id != loan.book.id:
                if book_selected.stock <= 0:
                    return render(
                        request,
                        "pages/loans/edit_loan.html",
                        {**context, "error": "Book out of stock."},
                    )

                # Aumentar el stock del libro recibido/cambiado
                loan.book.stock += 1
                loan.book.save()
                # Restar al stock del nuevo libro prestado
                book_selected.stock -= 1
                book_selected.save()

            loan.book_id = book_id
            loan.user_id = user_id
            loan.due_date = due_date
            if return_date:
                loan.return_date = return_date

            loan.save()
            return render(
                request,
                "pages/loans/edit_loan.html",
                {**context, "success": "Loan updated successfully."},
            )
        except Exception as e:
            return render(
                request,
                "pages/loans/edit_loan.html",
                {**context, "error": "An error occurred while updating the loan."},
            )

    return render(request, "pages/loans/edit_loan.html", context)
