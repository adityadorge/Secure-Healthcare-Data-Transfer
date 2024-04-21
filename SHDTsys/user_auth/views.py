from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html', {})


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

