from django.shortcuts import render, redirect
from ...models import User
from django.contrib.auth.decorators import login_required


@login_required
def view_member(request, member_id):
    # Son permitidos los roles "admin" y "librarian", los usuarios "lector" no pueden ver la vista.
    if request.user.role == "lector":
        return redirect("index")

    user_to_view = User.objects.filter(id=member_id).first()
    # Si no existe el usuario, redirige a la lista de miembros
    if not user_to_view:
        return redirect("members")

    context = {"user": user_to_view}

    return render(request, "pages/members/view_member.html", context)
