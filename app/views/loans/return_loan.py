from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from ...models import Loan


@login_required
def return_loan(request, loan_id):
    # TODO: al devolver un libro, se debe reintegrar al stock de libros
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

    try:
        loan.return_date = return_date
        loan.status = "returned"
        loan.save()
        return redirect("view_loan", loan_id)
    except Exception as e:
        return JsonResponse({"message": "Error returning loan"})
