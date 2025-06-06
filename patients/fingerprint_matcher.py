import numpy as np
from scipy.spatial.distance import cdist
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from cryptography.fernet import Fernet
import pickle
import os
from django.conf import settings

class FastFingerprintMatcher:
    def __init__(self):
        self.model = self._init_model()
        self.encryption_key = settings.FERNET_SECRET_KEY.encode()
        self.cipher = Fernet(self.encryption_key)

    def _init_model(self):
        """Initialize optimized feature extraction model"""
        base_model = VGG16(weights='imagenet', include_top=False, pooling='avg')
        return Model(inputs=base_model.input, outputs=base_model.output)
    
    def extract_features(self, image_stream):
        """Extract fingerprint features efficiently"""
        img = image.load_img(image_stream, target_size=(224, 224))
        x = image.img_to_array(img)
        x = preprocess_input(x)
        features = self.model.predict(np.array([x]))[0]
        return features / np.linalg.norm(features)  # Normalize vector

    
    def encrypt_data(self, data):
        """Encrypt sensitive data"""
        return self.cipher.encrypt(pickle.dumps(data))
    
    def decrypt_data(self, encrypted_data):
        """Decrypt stored data"""
        return pickle.loads(self.cipher.decrypt(encrypted_data))
    
    def find_closest_match(self, query_embedding):
        from .models import PatientRecord
        all_patients = PatientRecord.objects.all()
        if not all_patients:
            return None

        embeddings = []
        patients = []
        for p in all_patients:
            try:
                emb = pickle.loads(p.fingerprint_embedding)
                if emb is not None and len(emb) == len(query_embedding):
                    embeddings.append(emb)
                    patients.append(p)
            except Exception as e:
                continue  # skip bad records

        if not embeddings:
            return None

        distances = cdist([query_embedding], embeddings, 'cosine')[0]
        min_idx = np.argmin(distances)
        
        if distances[min_idx] < 0.3:  # Experiment with this threshold
            patient = patients[min_idx]
            patient.match_confidence = 1 - distances[min_idx]
            return patient
        return None
