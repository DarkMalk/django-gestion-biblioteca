from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def loans(request):
    mock_data = [
        {
            "book_title": "1984",
            "user_name": "Carlos Perez",
            "request_date": datetime.strptime("2025-04-01", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-15", "%Y-%m-%d").date(),
            "return_date": datetime.strptime("2025-04-10", "%Y-%m-%d").date(),
            "status": "returned",
        },
        {
            "book_title": "Clean Code",
            "user_name": "Ana Gomez",
            "request_date": datetime.strptime("2025-03-20", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-03", "%Y-%m-%d").date(),
            "return_date": None,
            "status": "overdue",
        },
        {
            "book_title": "The Hobbit",
            "user_name": "Luis Rojas",
            "request_date": datetime.strptime("2025-03-25", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-08", "%Y-%m-%d").date(),
            "return_date": datetime.strptime("2025-04-07", "%Y-%m-%d").date(),
            "status": "returned",
        },
        {
            "book_title": "Sapiens",
            "user_name": "Maria Lopez",
            "request_date": datetime.strptime("2025-03-28", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-11", "%Y-%m-%d").date(),
            "return_date": None,
            "status": "overdue",
        },
        {
            "book_title": "The Pragmatic Programmer",
            "user_name": "Diego Rivera",
            "request_date": datetime.strptime("2025-04-05", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-19", "%Y-%m-%d").date(),
            "return_date": datetime.strptime("2025-04-17", "%Y-%m-%d").date(),
            "status": "returned",
        },
        {
            "book_title": "A Brief History of Time",
            "user_name": "Fernanda Martinez",
            "request_date": datetime.strptime("2025-03-18", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-01", "%Y-%m-%d").date(),
            "return_date": None,
            "status": "overdue",
        },
        {
            "book_title": "To Kill a Mockingbird",
            "user_name": "Javier Torres",
            "request_date": datetime.strptime("2025-03-30", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-13", "%Y-%m-%d").date(),
            "return_date": datetime.strptime("2025-04-10", "%Y-%m-%d").date(),
            "status": "returned",
        },
        {
            "book_title": "Python Crash Course",
            "user_name": "Laura Herrera",
            "request_date": datetime.strptime("2025-04-24", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-05-08", "%Y-%m-%d").date(),
            "return_date": None,
            "status": "active",
        },
        {
            "book_title": "The Art of War",
            "user_name": "Ricardo Vargas",
            "request_date": datetime.strptime("2025-03-15", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-03-29", "%Y-%m-%d").date(),
            "return_date": datetime.strptime("2025-03-28", "%Y-%m-%d").date(),
            "status": "returned",
        },
        {
            "book_title": "The Lean Startup",
            "user_name": "Gabriela Molina",
            "request_date": datetime.strptime("2025-03-30", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-13", "%Y-%m-%d").date(),
            "return_date": None,
            "status": "overdue",
        },
        {
            "book_title": "The Little Prince",
            "user_name": "Tomas Castillo",
            "request_date": datetime.strptime("2025-04-20", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-05-04", "%Y-%m-%d").date(),
            "return_date": None,
            "status": "active",
        },
        {
            "book_title": "One Hundred Years of Solitude",
            "user_name": "Sofia Mendez",
            "request_date": datetime.strptime("2025-03-26", "%Y-%m-%d").date(),
            "due_date": datetime.strptime("2025-04-09", "%Y-%m-%d").date(),
            "return_date": None,
            "status": "overdue",
        },
    ]

    status = request.GET.get("status")

    if status in ["active", "overdue", "returned"]:
        mock_data = [loan for loan in mock_data if loan["status"] == status]

    paginator = Paginator(mock_data, 5)  # Mostrar 5 prestamos por pagina
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "pages/loans.html", context={"loans": page_obj})
