def total_stock_per_book(books, loan):
    total_stock = {}

    for book in books:
        total_stock[book.id] = {
            "title": book.title,
            "author": book.author.name,
            "total_stock": book.stock
            + loan.filter(book=book, status__in=["active", "overdue"]).count(),
            "available_stock": book.stock,
        }

    return total_stock
