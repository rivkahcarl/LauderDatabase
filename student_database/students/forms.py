from django import forms
from django.contrib.auth.models import User

from students.models import StaffContact


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'password': forms.PasswordInput()}


class StaffContactForm(forms.ModelForm):
    class Meta:
        model = StaffContact
        fields = ('note', 'conversation_date_time', 'student')
        widgets = {"student": forms.HiddenInput()}
