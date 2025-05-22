from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from ...models import Loan


@login_required
def view_loan(request, loan_id):
    if request.user.role == "lector":
        loan = Loan.objects.filter(id=loan_id, user=request.user).first()
    else:
        loan = Loan.objects.filter(id=loan_id).first()

    if not loan:
        return redirect("loans")

    today = datetime.today().date()
    remaining_days = loan.due_date - today

    context = {
        "loan": loan,
        "remaining_days": remaining_days.days,
        "today": today,
    }

    return render(request, "pages/loans/view_loan.html", context)
