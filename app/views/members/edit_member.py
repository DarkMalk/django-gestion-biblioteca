from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ...models import User


@login_required
def edit_member(request, member_id):
    # Vista restringida para usuarios lectores
    if request.user.role == "lector":
        return redirect("index")

    roles = User.ROLE_CHOICES
    member = User.objects.filter(id=member_id).first()

    if not member:
        return redirect("members")

    context = {"roles": roles, "member": member}

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        role = request.POST.get("role")
        active = request.POST.get("status")

        if not all([username, email, first_name, last_name, role, active]):
            return render(
                request,
                "pages/members/edit_member.html",
                {**context, "error": "All fields are required"},
            )

        if role not in [role[0] for role in User.ROLE_CHOICES]:
            return render(
                request,
                "pages/members/edit_member.html",
                {**context, "error": "Invalid role"},
            )

        if User.objects.filter(username=username).exclude(id=member_id).exists():
            return render(
                request,
                "pages/members/edit_member.html",
                {**context, "error": "Username already exists"},
            )

        try:
            member.username = username
            member.email = email
            member.first_name = first_name
            member.last_name = last_name
            member.is_active = active

            print(member.is_active)

            # Si el usuario autenticado es bibliotecario, no puede cambiar a un rol que no sea lector. -> en UI se encuentra bloqueado el select para usuarios que no sean admin
            if (
                request.user.role == "librarian"
                and not role
                in [
                    role[0]
                    for role in roles
                    if role[0] != "admin" and role[0] != "librarian"
                ]
                and member.role != role
            ):
                return render(
                    request,
                    "pages/members/edit_member.html",
                    {
                        **context,
                        "error": "User does not have permission to edit this role",
                    },
                )

            member.role = role

            if password:
                member.password = password

            member.save()
            return render(
                request,
                "pages/members/edit_member.html",
                {**context, "success": "Member updated successfully"},
            )

        except Exception as e:
            return render(
                request,
                "pages/members/edit_member.html",
                {**context, "error": "Error updating member"},
            )

    return render(request, "pages/members/edit_member.html", context)
