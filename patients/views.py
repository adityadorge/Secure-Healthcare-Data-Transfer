from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import PatientRecord
# from .serializers import PatientRecordSerializer
from .fingerprint_matcher import FastFingerprintMatcher
from cryptography.fernet import Fernet
import pickle
import numpy as np
from io import BytesIO
import json
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html', {})

# Initialize fingerprint matcher
matcher = FastFingerprintMatcher()

@api_view(['POST'])
def enroll_patient(request):
    print("Endpoint for enrolling new patients")
    try:
        patient_id = request.POST.get('patient_id')
        medical_data_raw = request.POST.get('medical_data')
        print("Raw medical data:", medical_data_raw)
        fingerprint = request.FILES['fingerprint'].read()

        # Process and store securely
        embedding = matcher.extract_features(BytesIO(fingerprint))
        medical_data = json.loads(medical_data_raw)  # Safely convert to dict
        encrypted_data = matcher.encrypt_data(medical_data)
        
        
        PatientRecord.objects.create(
            patient_id=patient_id,
            fingerprint_embedding=pickle.dumps(embedding),
            encrypted_data=encrypted_data,
        )
        
        return JsonResponse({'status': 'success', 'patient_id': patient_id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

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
