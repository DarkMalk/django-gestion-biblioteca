from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth(request, user)
            return redirect(request.GET.get("next", "books"))
        else:
            return render(request, "pages/login.html", {"error": "Invalid credentials"})

    return render(request, "pages/login.html")
