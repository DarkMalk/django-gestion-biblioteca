from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import Editorial


@login_required
def add_publisher(request):
    if request.user.role == "lector":
        return redirect("index")

    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        email = request.POST.get("email")

        if not name:
            return render(
                request,
                "pages/publishers/add_publisher.html",
                {"error": "Name is required"},
            )

        if Editorial.objects.filter(name=name).exists():
            return render(
                request,
                "pages/publishers/add_publisher.html",
                {"error": "Publisher already exists"},
            )

        try:
            Editorial.objects.create(name=name, address=address, email=email)
            return render(
                request,
                "pages/publishers/add_publisher.html",
                {"success": "Publisher added successfully"},
            )
        except Exception as e:
            return render(
                request,
                "pages/publishers/add_publisher.html",
                {"error": "An error occurred while adding the publisher"},
            )

    return render(request, "pages/publishers/add_publisher.html")
