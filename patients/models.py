from django.db import models
import numpy as np
import pickle

class PatientRecord(models.Model):
    # patient_id = models.CharField(max_length=100, unique=True)
    fingerprint_embedding = models.BinaryField()  # Stores pickled numpy array
    encrypted_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Cache for faster access
    match_confidence = None
    
    class Meta:
        indexes = [
            models.Index(fields=['patient_id']),
        ]
        
    def get_embedding(self):
        """Lazy-load the fingerprint embedding"""
        return pickle.loads(self.fingerprint_embedding)