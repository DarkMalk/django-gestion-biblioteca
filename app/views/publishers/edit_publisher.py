from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import Editorial


@login_required
def edit_publisher(request, publisher_id):
    if request.user.role == "lector":
        return redirect("index")

    publisher = Editorial.objects.filter(id=publisher_id).first()
    if not publisher:
        return redirect("publishers")

    context = {
        "publisher": publisher,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        email = request.POST.get("email")

        if not name:
            return render(
                request,
                "pages/publishers/edit_publisher.html",
                {**context, "error": "Name is required"},
            )

        if Editorial.objects.filter(name=name).exclude(id=publisher_id).exists():
            return render(
                request,
                "pages/publishers/edit_publisher.html",
                {**context, "error": "Publisher already exists"},
            )

        try:
            publisher.name = name
            publisher.address = address
            publisher.email = email
            publisher.save()
            return render(
                request,
                "pages/publishers/edit_publisher.html",
                {**context, "success": "Publisher updated successfully"},
            )
        except Exception as e:
            return render(
                request,
                "pages/publishers/edit_publisher.html",
                {**context, "error": "An error occurred while updating the publisher"},
            )

    return render(request, "pages/publishers/edit_publisher.html", context)
