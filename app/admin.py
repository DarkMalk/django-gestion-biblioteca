from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(User, UserAdmin)
