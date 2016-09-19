from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from homepage.forms import RegistrationForm


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data()
        context['login_form'] = AuthenticationForm()
        context['signup_form'] = RegistrationForm()
        return context


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect(reverse_lazy('home:homepage'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home:homepage'))


def registration_view(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password)
        user = authenticate(username=username, password=password)
        login(request, user)
    return HttpResponseRedirect(reverse_lazy('home:homepage'))
