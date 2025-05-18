from django import forms
from .models import Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulaire pour réserver un rendez-vous
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'cin_number', 'description']

# Formulaire d'inscription
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
