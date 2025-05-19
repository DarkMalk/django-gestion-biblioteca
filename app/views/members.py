from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import User
from django.core.paginator import Paginator


@login_required
def members(request):
    members = User.objects.all()

    status = request.GET.get("status")
    search = request.GET.get("search")

    if search:
        members = members.filter(username__icontains=search)

    if status in ["active", "suspended"]:
        members = members.filter(is_active=(status == "active"))

    paginator = Paginator(members, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "pages/members.html", context={"members": page_obj})
