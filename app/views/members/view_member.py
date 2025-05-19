from django.http import HttpResponse


def view_member(request, member_id):
    return HttpResponse(f"Viewing member with ID: {member_id}")
