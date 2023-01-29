from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Books


# Register your models here.

class booksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(Books, booksAdmin)


