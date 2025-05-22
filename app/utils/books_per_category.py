def books_per_category(books):
    books_by_category = {}

    for book in books:
        category = book.category.name
        if category in books_by_category:
            books_by_category[category] += 1
        else:
            books_by_category[category] = 1

    return books_by_category
