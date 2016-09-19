from django.views.generic import TemplateView


class Students(TemplateView):
    template_name = 'students/students_home.html'
