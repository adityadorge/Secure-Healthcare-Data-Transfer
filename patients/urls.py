from django.urls import path
from . import views

app_name = 'patients'  # This sets the namespace

urlpatterns = [
    path('', views.home, name='home'),  # This is the view we're redirecting to
    # ... other patient app URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enroll/', views.enroll_patient, name='enroll_patient'),
    path('verify/', views.verify_patient, name='verify_patient'),
]