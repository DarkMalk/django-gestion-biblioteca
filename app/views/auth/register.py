from ...models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json


def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        email = data.get("email")
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if not all(
            [email, username, first_name, last_name, password, confirm_password]
        ):
            return JsonResponse({"error": "All fields are required"}, status=400)

        if password != confirm_password:
            return JsonResponse({"error": "Passwords do not match"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        if user is not None:
            return redirect("login")
        else:
            return JsonResponse({"error": "User creation failed"}, status=500)

    # GET request
    return render(request, "pages/register.html")
