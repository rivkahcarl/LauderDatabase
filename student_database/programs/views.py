from django.views.generic import TemplateView


class Programs(TemplateView):
    template_name = 'programs/programs_home.html'
