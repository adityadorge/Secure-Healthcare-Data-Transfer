from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
# , UserDetailsForm
# from .models import UserDetail


def home(request):
    return render(request, 'home.html', {})


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = authenticate(request, email=email, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login success"))
            return redirect('home')
        else:
            messages.error(request, ("There was error please try again"))
            return redirect('login')
    else:
        return render(request, 'user_auth/login.html', {})


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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, ("Account Created"))
            return redirect('home')
        else:
            messages.error(request, ("Error please try again later"))
            return redirect('register')
    else:
        return render(request, 'user_auth/register.html', {'form': form})


# def user_detail(request):
#     user = request.user
#     user_name = request.user.name
#     user_details = UserDetail.objects.filter(user=request.user).first()
#     form = UserDetailsForm(initial={'name': user_name} ,instance=user_details) # Pre-populate with existing details (if any)
#     if request.method == 'POST':
#         form = UserDetailsForm(request.POST, request.FILES, instance=user_details)
#         print(request.POST)
#         print(form.errors)
#         if form.is_valid():
#             form.instance.user = request.user 
#             form.save()
#             if 'name' in form.cleaned_data:
#                 user.name = form.cleaned_data['name']
#                 user.save()
#             messages.success(request, ("Form submitted successfully"))
#             return redirect('home')
#         else:
#             messages.error(request, (f"Error: {form.errors} "))
#             return render(request, 'user_details/user_details_form.html', {'form': form})
#     else:
#         return render(request, 'user_details/user_details_form.html', {'form': form})
