from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *

def home(request):
    return render(request, 'home/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_obj = form.cleaned_data
            fullname = user_obj.get('fullname')
            messages.success(request, f'{fullname}, Succesfully created your account!')
            return redirect('evoting-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

def profile(request):
    return render(request, 'profile.html', {'username': request.user.username})
