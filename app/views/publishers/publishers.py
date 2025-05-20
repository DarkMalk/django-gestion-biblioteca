from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ...models import Editorial


@login_required
def publishers(request):
    if request.user.role == "lector":
        return redirect("index")

    publishers = Editorial.objects.all()

    search = request.GET.get("search")

    if search:
        publishers = publishers.filter(name__icontains=search)

    paginator = Paginator(publishers, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "publishers": page_obj,
    }

    return render(request, "pages/publishers/publishers.html", context)
