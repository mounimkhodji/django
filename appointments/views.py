from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import AppointmentForm, RegisterForm
from .models import Appointment
from django.contrib.auth.decorators import login_required


# Page d'accueil
def home(request):
    return render(request, 'appointments/home.html')
# Connexion utilisateur
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'appointments/login.html', {'form': form})

# Inscription utilisateur
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'appointments/register.html', {'form': form})

# Réservation de rendez-vous
@login_required
def booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/booking.html', {'form': form})

