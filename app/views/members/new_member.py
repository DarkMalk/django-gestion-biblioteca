from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import User


@login_required
def new_member(request):
    if request.user.role == "lector":
        return redirect("index")

    context = {
        "roles": User.ROLE_CHOICES,
    }

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        role = request.POST.get("role")
        active = request.POST.get("status")

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "pages/members/new_member.html",
                {**context, "error": "Username already exists"},
            )

        if not all([username, password, first_name, last_name, email, role, active]):
            return render(
                request,
                "pages/members/new_member.html",
                {**context, "error": "All fields are required"},
            )

        if role not in [role[0] for role in User.ROLE_CHOICES]:
            return render(
                request,
                "pages/members/new_member.html",
                {**context, "error": "Invalid role"},
            )

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                role=role,
                is_active=active,
            )

            user.save()

            return render(
                request,
                "pages/members/new_member.html",
                {**context, "success": "User created successfully"},
            )
        except Exception as e:
            return render(
                request,
                "pages/members/new_member.html",
                {**context, "error": "Error creating user"},
            )

    return render(request, "pages/members/new_member.html", context)
