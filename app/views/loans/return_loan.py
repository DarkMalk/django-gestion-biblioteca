from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from ...models import Loan, Book


@login_required
def return_loan(request, loan_id):
    if request.user.role == "lector":
        return redirect("index")

    if request.method != "POST":
        return JsonResponse({"message": "Method not available"})

    loan = Loan.objects.filter(id=loan_id).first()
    if not loan:
        return JsonResponse({"message": "Loan not found"})

    if loan.status == "returned":
        return JsonResponse({"message": "Loan already returned"})

    return_date = request.POST.get("return_date")
    if not return_date:
        return JsonResponse({"message": "Return date is required"})

    book = Book.objects.filter(id=loan.book.id).first()

    if not book:
        return JsonResponse({"message": "Book not found"})

    try:
        loan.return_date = return_date
        loan.status = "returned"
        book.stock += 1

        loan.save()
        book.save()
        return redirect("view_loan", loan_id)
    except Exception as e:
        return JsonResponse({"message": "Error returning loan"})
