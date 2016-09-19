from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    """ TODO-Benny: add check in clean() for already existing username """
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'password': forms.PasswordInput()}
