from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import books


# Register your models here.

class booksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(books, booksAdmin)


