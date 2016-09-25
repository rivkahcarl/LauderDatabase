from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from students.models import Student


class Students(ListView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    success_url = reverse_lazy('students:students-list')
    fields = ['event_name', 'event_start_date_time', 'event_end_date_time',
              'event_address', 'event_city', 'event_state', 'event_zip',
              'event_theme']
