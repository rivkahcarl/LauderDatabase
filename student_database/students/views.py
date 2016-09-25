from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from students.models import Student


STUDENT_FIELDS = ['first_name', 'last_name', 'address',
                  'city', 'state', 'gender', 'zip',
                  'age', 'country']


class Students(ListView):
    model = Student


class StudentCreate(CreateView):
    model = Student
    success_url = reverse_lazy('students:students-list')
    fields = STUDENT_FIELDS


class StudentUpdate(UpdateView):
    model = Student
    fields = STUDENT_FIELDS
    template_name_suffix = '_update_form'
