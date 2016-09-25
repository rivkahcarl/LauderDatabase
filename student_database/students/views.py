from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from students.models import Student


class Students(ListView):
    model = Student


class StudentCreate(CreateView):
    model = Student
    success_url = reverse_lazy('students:students-list')
    fields = ['first_name', 'last_name', 'address',
              'city', 'state', 'gender', 'zip',
              'age', 'country']
