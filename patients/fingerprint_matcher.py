import numpy as np
from scipy.spatial.distance import cdist
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from cryptography.fernet import Fernet
import pickle
from django.conf import settings


class FastFingerprintMatcher:
    def __init__(self):
        self.model = self._init_model()
        self.encryption_key = settings.FERNET_SECRET_KEY.encode()
        self.cipher = Fernet(self.encryption_key)

    def _init_model(self):
        """Initialize pre-trained CNN model for feature extraction"""
        base_model = VGG16(weights='imagenet', include_top=False, pooling='avg')
        return Model(inputs=base_model.input, outputs=base_model.output)

    def extract_features(self, image_stream):
        """Extract fingerprint features and normalize"""
        img = image.load_img(image_stream, target_size=(224, 224))
        x = image.img_to_array(img)
        x = preprocess_input(x)
        features = self.model.predict(np.array([x]))[0]
        return features / np.linalg.norm(features)

    def encrypt_data(self, data):
        """Encrypt serialized data"""
        return self.cipher.encrypt(pickle.dumps(data))

    def decrypt_data(self, encrypted_data):
        """Decrypt and deserialize data"""
        return pickle.loads(self.cipher.decrypt(encrypted_data))

    def find_closest_match(self, query_embedding, threshold=0.1):
        """
        Find the closest patient using cosine distance.
        Only return match if distance < threshold (i.e. similarity > 0.7)
        """
        from .models import PatientRecord

        all_patients = PatientRecord.objects.all()
        if not all_patients:
            return None

        embeddings = []
        patients = []

        for p in all_patients:
            try:
                emb = pickle.loads(p.fingerprint_embedding)
                if emb is not None and emb.shape == query_embedding.shape:
                    embeddings.append(emb)
                    patients.append(p)
            except Exception as e:
                # Skip corrupted records silently or log it
                continue

        if not embeddings:
            return None

        distances = cdist([query_embedding], embeddings, metric='cosine')[0]
        min_idx = np.argmin(distances)
        min_distance = distances[min_idx]

        if min_distance < threshold:
            best_match = patients[min_idx]
            best_match.match_confidence = round(1 - min_distance, 3)  # Optional: attach confidence
            return best_match

        return None  # No suitable match found
