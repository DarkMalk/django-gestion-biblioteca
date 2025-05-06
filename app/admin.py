from django.contrib import admin
from .models import (
    Author,
    Book,
    Category,
    Editorial,
    Loan,
    AuthorAdmin,
    CategoryAdmin,
    BookAdmin,
    EditorialAdmin,
    LoanAdmin,
)

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Loan, LoanAdmin)
