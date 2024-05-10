from django.urls import path
from . import views

# app_name = "user_auth"
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/two-factor/send_otp/', views.send_otp, name='send_otp'),
    path('accounts/two-factorverify_otp/', views.verify_otp, name='verify_otp'),
]