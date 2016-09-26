from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from programs.models import Program


PROGRAM_FORM_FIELDS = ['event_name', 'event_start_date_time',
                       'event_end_date_time', 'event_address', 'event_city',
                       'event_state', 'event_zip', 'event_theme']


class Programs(ListView):
    model = Program


class ProgramCreate(CreateView):
    model = Program
    success_url = reverse_lazy('programs:programs-list')
    fields = PROGRAM_FORM_FIELDS


class ProgramUpdate(UpdateView):
    model = Program
    fields = PROGRAM_FORM_FIELDS
    template_name_suffix = '_update_form'
