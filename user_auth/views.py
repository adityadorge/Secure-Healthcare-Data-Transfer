from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.urls import reverse

def home(request):
    # Check if user is authenticated (optional)
    if request.user.is_authenticated:
        # Redirect to patient app's main page
        return redirect(reverse('patients:home'))  # Using URL namespace
    else:
        # If not authenticated, you might want to redirect to login
        return render(request, 'home.html', {})  # Or render your home.html if it's a landing page


