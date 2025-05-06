from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Loan


@login_required
def loans(request):
    loans = Loan.objects.all()

    status = request.GET.get("status")

    if status in [choice[0] for choice in Loan.STATUS_CHOICES]:
        loans = loans.filter(status=status)

    paginator = Paginator(loans, 5)  # Mostrar 5 prestamos por pagina
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "pages/loans.html", context={"loans": page_obj})
