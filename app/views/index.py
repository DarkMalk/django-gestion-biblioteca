from django.shortcuts import render

mock_data = {
    "user": {"name": "Admin Librarian", "email": "admin@library.com"},
    "books": {"total_books": 1248, "added_month": 12},
    "loans": {
        "active_loans": 145,
        "active_from_last_week": 22,
        "overdue_loans": 12,
        "overdue_from_last_week": 4,
    },
    "members": {"total_members": 573, "new_members": 18},
    "new_members_last_seven_months": {
        "Jan": 12,
        "Feb": 15,
        "Mar": 32,
        "Apr": 18,
        "May": 14,
        "Jun": 11,
        "Jul": 9,
    },
}


def index(request):
    return render(request, "pages/index.html", context=mock_data)
