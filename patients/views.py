from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import PatientRecord
# from .serializers import PatientRecordSerializer
from .fingerprint_matcher import FastFingerprintMatcher
from cryptography.fernet import Fernet
import pickle, json
import numpy as np
from io import BytesIO
from django.shortcuts import render, redirect
from .forms import PatientEnrollmentForm 


def home(request):
    return render(request, 'home.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

# Initialize fingerprint matcher
matcher = FastFingerprintMatcher()

# @api_view(['POST'])
def enroll_patient(request):
    if request.method == 'GET':
        form = PatientEnrollmentForm()
        return render(request, 'enroll_form.html', {'form': form})
    
    elif request.method == 'POST':
        form = PatientEnrollmentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                patient_id = form.cleaned_data['patient_id']
                medical_data_dict = {
                    'name': form.cleaned_data['name'],
                    'age': form.cleaned_data['age'],
                    'gender': form.cleaned_data['gender'],
                    'address': form.cleaned_data['address'],
                    'notes': form.cleaned_data['notes'],
                }
                fingerprint_file = request.FILES['fingerprint'].read()

                # Extract and encrypt
                embedding = matcher.extract_features(BytesIO(fingerprint_file))
                encrypted_data = matcher.encrypt_data(medical_data_dict)

                # Save
                PatientRecord.objects.create(
                    patient_id=patient_id,
                    fingerprint_embedding=pickle.dumps(embedding),
                    encrypted_data=encrypted_data,
                )
                return JsonResponse({'status': 'success', 'patient_id': patient_id})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'}, status=400)

@api_view(['POST'])
def verify_patient(request):
    print("Verifying patient from fingerprint...")
    try:
        fingerprint = request.FILES['fingerprint'].read()
        embedding = matcher.extract_features(BytesIO(fingerprint))
        patient = matcher.find_closest_match(embedding)

        if patient:
            decrypted_data = matcher.decrypt_data(patient.encrypted_data)
            return JsonResponse({
                'status': 'success',
                'patient_id': patient.patient_id,
                'medical_data': decrypted_data,  # if already dict
                'confidence': patient.match_confidence
            }, safe=False)
        else:
            return JsonResponse({'status': 'not_found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


from django.shortcuts import render
from .forms import FingerprintFetchForm
from .models import PatientRecord
import pickle

def verify_patient(request):
    if request.method == 'POST':
        form = FingerprintFetchForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                fingerprint = request.FILES['fingerprint'].read()
                embedding = matcher.extract_features(BytesIO(fingerprint))
                patient = matcher.find_closest_match(embedding)

                if patient:
                    decrypted_data = matcher.decrypt_data(patient.encrypted_data)
                    return render(request, 'fetch_report.html', {
                        'form': form,
                        'medical_data': decrypted_data
                    })
                else:
                    return render(request, 'fetch_report.html', {
                        'form': form,
                        'error': 'No matching record found.'
                    })
            except Exception as e:
                return render(request, 'fetch_report.html', {
                    # 'form': form,
                    'error': f'Error processing fingerprint: {e}'
                })
    else:
        form = FingerprintFetchForm()
    return render(request, 'fetch_report.html', {'form': form})
