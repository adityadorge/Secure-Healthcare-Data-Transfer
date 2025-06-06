import requests
from io import BytesIO
import json

SERVER_URL = "http://127.0.0.1:8000/"

def enroll_patient(patient_id, fingerprint_path, medical_data):  
    print("Client function to enroll patient")
    with open(fingerprint_path, 'rb') as f:
        files = {'fingerprint': f}
        data = {
            'patient_id': patient_id,
            'medical_data': medical_data
        }
        response = requests.post(f"{SERVER_URL}patients/enroll/", files=files, data=data)
    return response.json()

def verify_patient(fingerprint_path):
    print("Client function to verify and retrieve patient data")
    with open(fingerprint_path, 'rb') as f:
        files = {'fingerprint': f}
        response = requests.post(f"{SERVER_URL}patients/verify/", files=files)
    return response.json()

# Example usage
if __name__ == "__main__":
    #Enroll a patient
    # enroll_response = enroll_patient(
    #     patient_id="P1002",
    #     fingerprint_path="/home/aditya/Projects/Secure-Healthcare-Data-Transfer/data_check/same_1/101_6.tif",
    #     medical_data=json.dumps({"name": "John Doe","conditions": ["hypertension"]})
    # )
    # print(enroll_response)
    
    # # Verify a patient
    verify_response = verify_patient("/home/aditya/Projects/Secure-Healthcare-Data-Transfer/data_check/same_1/101_6.tif")
    print(verify_response)