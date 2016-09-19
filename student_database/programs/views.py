from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from programs.models import Program


class Programs(ListView):
    model = Program


class ProgramCreate(CreateView):
    model = Program
    success_url = reverse_lazy('programs:programs-list')
    fields = ['event_name', 'event_start_date_time', 'event_end_date_time',
              'event_address', 'event_city', 'event_state', 'event_zip',
              'event_theme']
