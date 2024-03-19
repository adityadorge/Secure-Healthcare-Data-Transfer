from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login success"))
            return redirect('home')
        else:
            messages.error(request, ("There was error please try again"))
            return redirect('login')
    else:
        return render(request,'user_auth/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out!"))
    return redirect('login')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Account Created"))
            return redirect('home')
        else:
            messages.error(request, ("Error please try again later"))
            return redirect('register')
    else:
        return render(request, 'user_auth/register.html', {'form':form})