from django.contrib import admin
from .models import (AcademicSession,
                     Term, Department,
                     Batch, TempSerialID,
                     Subject)


class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('year', 'created_by')


class BatchAdmin(admin.ModelAdmin):
    list_display = ('year', 'number', 'department',)


class TempSerialIDAdmin(admin.ModelAdmin):
    list_display = ('year', 'serial', 'department', 'student')


admin.site.register(AcademicSession, AcademicSessionAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(TempSerialID, TempSerialIDAdmin)
admin.site.register(Term)
admin.site.register(Department)
admin.site.register(Subject)