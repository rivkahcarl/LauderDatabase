from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from students.models import Student, StaffContact
from students.forms import StaffContactForm


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


class StaffContactCreate(CreateView):
    model = StaffContact
    form_class = StaffContactForm
    success_url = reverse_lazy('students:students-list')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        initials = {
            "student": self.kwargs['student_id']
        }
        form = form_class(initial=initials, data=self.request.POST or None)
        return form
