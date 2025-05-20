from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import Category


@login_required
def edit_category(request, category_id):
    if request.user.role == "lector":
        return redirect("index")

    category = Category.objects.filter(id=category_id).first()

    if not category:
        return redirect("categories")

    context = {"category": category}

    if request.method == "POST":
        name = request.POST.get("name")

        if not name:
            return render(
                request,
                "pages/categories/edit_category.html",
                {**context, "error": "All fields are required"},
            )

        if Category.objects.filter(name=name).exclude(id=category_id).exists():
            return render(
                request,
                "pages/categories/edit_category.html",
                {**context, "error": "Category already exists"},
            )

        try:
            category.name = name
            category.save()
            return render(
                request,
                "pages/categories/edit_category.html",
                {**context, "success": "Category updated successfully"},
            )
        except Exception as e:
            return render(
                request,
                "pages/categories/edit_category.html",
                {**context, "error": "An error occurred while updating the category"},
            )

    return render(request, "pages/categories/edit_category.html", context)
