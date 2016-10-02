from django.contrib import admin

from students.models import Student
from students.views import STUDENT_FIELDS


class StudentAdmin(admin.ModelAdmin):
    list_display = STUDENT_FIELDS


admin.site.register(Student, StudentAdmin)
