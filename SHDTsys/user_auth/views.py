import pyotp
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.conf import settings

from django.core.mail import send_mail

from django import forms

from .forms import SignUpForm
from .models import OTP, User



def home(request):
    return render(request, 'home.html', {})

def send_otp(request):
    current_site = get_current_site(request)
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            # Generate OTP
            otp_secret = pyotp.random_base32()
            otp = pyotp.TOTP(otp_secret)
            otp_code = otp.now()

            # Save OTP to the database
            otp_obj, created = OTP.objects.get_or_create(user=user, email=email)
            otp_obj.otp_secrete = otp_secret
            otp_obj.save()

            # Send OTP via email
            subject = f"{current_site.name} - Your OTP for Login"
            message = f"Your OTP for login is: {otp_code}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return redirect('verify_otp')
        else:
            return render(request, 'email_otp/send_otp.html', {'message':'Email not found'})
    else:
        return render(request, 'email_otp/send_otp.html')

def verify_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp_code = request.POST.get('otp')
        otp_obj = OTP.objects.filter(email=email).first()
    
        if otp_obj:
            otp = pyotp.TOTP(otp_obj.otp_secrete)
            print(otp_obj.otp_secrete)
            print(otp_code)
            print(otp.verify(otp_code))
            if otp.verify(otp_code):
                otp_obj.is_verified = True
                otp_obj.save
                user = authenticate(request, email=otp_obj.user.email, password='')

                if user:
                    login(request, user)
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    return redirect('/accounts/login')
            else:
                return render(request, 'email_otp/verify_otp.html', {'message': 'Invalid OTP'})
        else:
            return render(request, 'email_otp/verify_otp.html', {'message': 'OTP not found'})
    else:
        return render(request, 'email_otp/verify_otp.html')

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

