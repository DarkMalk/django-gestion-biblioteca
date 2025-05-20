from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ...models import Category


@login_required
def categories(request):
    if request.user.role == "lector":
        return redirect("index")

    categories = Category.objects.all()
    search = request.GET.get("search")

    if search:
        categories = categories.filter(name__icontains=search)

    paginator = Paginator(categories, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"categories": page_obj}

    return render(request, "pages/categories/categories.html", context)
