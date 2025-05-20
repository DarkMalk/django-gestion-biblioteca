from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import Category


@login_required
def add_category(request):
    if request.user.role == "lector":
        return redirect("index")

    if request.method == "POST":
        name = request.POST.get("name")

        if not name:
            return render(
                request,
                "pages/categories/add_category.html",
                {"error": "All fields are required"},
            )

        if Category.objects.filter(name=name).exists():
            return render(
                request,
                "pages/categories/add_category.html",
                {"error": "Category already exists"},
            )

        try:
            category = Category.objects.create(name=name)
            return render(
                request,
                "pages/categories/add_category.html",
                {"success": "Category created successfully"},
            )
        except Exception as e:
            return render(
                request,
                "pages/categories/add_category.html",
                {"error": "Error creating category"},
            )

    return render(request, "pages/categories/add_category.html")
