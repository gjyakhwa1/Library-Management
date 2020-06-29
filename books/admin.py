from django.contrib import admin
from .models import Books, IssueBooks
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Books)
class ViewAdmin(ImportExportModelAdmin):
    ordering = ['title']


admin.site.register(IssueBooks)
