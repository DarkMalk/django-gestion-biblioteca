from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Loan


@login_required
def loans(request):
    if request.user.groups.filter(name="bibliotecario").exists():
        loans = Loan.objects.all()
    else:
        loans = Loan.objects.filter(user=request.user)

    status = request.GET.get("status")
    search = request.GET.get("search")

    if search:
        loans = loans.filter(book__title__icontains=search)

    if status in [choice[0] for choice in Loan.STATUS_CHOICES]:
        loans = loans.filter(status=status)

    paginator = Paginator(loans, 5)  # Mostrar 5 prestamos por pagina
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "pages/loans.html", context={"loans": page_obj})
