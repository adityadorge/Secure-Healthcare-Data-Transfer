from django.contrib import admin
from .models import PatientRecord 
import pickle
import numpy as np
from .fingerprint_matcher import FastFingerprintMatcher
import json

# Create one shared matcher instance to reuse the key
matcher = FastFingerprintMatcher()

@admin.register(PatientRecord)
class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'created_at', 'updated_at', 'medical_data_preview')
    
    def medical_data_preview(self, obj):
        """Preview of decrypted medical JSON"""
        try:
            data = matcher.decrypt_data(obj.encrypted_data)
            if isinstance(data, dict):
                return data.get('name') or str(data)[:30]
            return str(data)[:30]
        except Exception:
            return "Unable to decrypt"
    medical_data_preview.short_description = "Decrypted Name / Preview"



