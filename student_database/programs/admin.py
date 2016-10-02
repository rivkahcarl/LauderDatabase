from django.contrib import admin

from programs.models import Program
from programs.views import PROGRAM_FORM_FIELDS


class ProgramAdmin(admin.ModelAdmin):
    list_display = PROGRAM_FORM_FIELDS


admin.site.register(Program, ProgramAdmin)
