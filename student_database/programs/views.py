from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
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


class AddStudents(TemplateView):
    template_name = "programs/add_students.html"

    def get_context_data(self, **kwargs):
        ctx = super(AddStudents, self).get_context_data(**kwargs)
        ctx['program_pk'] = kwargs['pk']
        ctx['program_title'] = Program.objects.get(pk=kwargs['pk']).event_name
        return ctx
