from django.db import models
from user_auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Prefer not to say', 'Prefer not to say'),
)

SEVERITY_CHOICES = (
    ('Not Defined', 'Not Defined'),
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('Extreme','Extreme'),
)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    phone_number = models.CharField(max_length=20, blank = True)
    date_of_birth = models.DateField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=20, blank=True, choices=GENDER_CHOICES, default='Prefer not to say')
    emergency_contact_info = models.CharField(max_length=20, blank=True)

class Patient_medical_history(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # Past Surgeries and Procedures
    procedure_name = models.CharField(max_length=60, blank=True)
    procedure_date = models.DateField(blank=True, null=True)
    operator_name = models.CharField(max_length=60, blank=True)
    procedure_hospital = models.CharField(max_length=255, blank=True)
    procedure_report = models.FileField(null=True, blank=True)

    # Social History
    smoking_status = models.CharField(max_length=20, blank=True, choices=SEVERITY_CHOICES, default='Not Defined')
    alcohol_status = models.CharField(max_length=20, blank=True, choices=SEVERITY_CHOICES, default='Not Defined')
    illegal_items_status = models.CharField(max_length=20, blank=True, choices=SEVERITY_CHOICES, default='Not Defined')
    other_social_factors = models.TextField(max_length=255, blank=True)

    # Family History
    relative_name = models.CharField(max_length=100, blank=True)
    relationship = models.CharField(max_length=60, blank=True)
    relative_medical_condition = models.CharField(max_length=100, blank=True)


class Medication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  


class Patient_medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255)   
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    reason_for_use = models.TextField(max_length=255, blank=True)
    severity = models.CharField(max_length=20, blank=True, choices=SEVERITY_CHOICES, default='Not Defined')


class Disease(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    caused_by = models.TextField(max_length=255, blank=True)
    Reaction = models.TextField(max_length=255, blank=True)
    severity = models.CharField(max_length=20, blank=True, choices=SEVERITY_CHOICES, default='Not Defined')

class Patient_disease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    onset_date = models.DateField(blank=True, null=True)
    severity = models.CharField(max_length=20, blank=True, choices=SEVERITY_CHOICES, default='Not Defined')

    class Meta:
        unique_together = (('patient', 'disease'),)

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, blank=True)
    target_disease = models.CharField(max_length=255, blank=True)
    recommended_doses = models.PositiveIntegerField(blank=True, null=True)

class Patient_vaccination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    vaccine_date = models.DateField(blank=True, null=True)
    dose_number = models.PositiveIntegerField(blank=True, null=True)
    next_dose_due = models.DateField(blank=True, null=True)
    notes = models.TextField(max_length=255, blank=True)

class LabTest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)

class LabReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    lab_name = models.CharField(max_length=255)
    order_date = models.DateField()
    report_date = models.DateField()
    accession_number = models.CharField(max_length=255)
    report_copy = models.FileField(upload_to='lab_reports/', blank=True)

class LabResult(models.Model):
    lab_report = models.ForeignKey(LabReport, on_delete=models.CASCADE)
    test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    result_value = models.CharField(max_length=255)
    reference_range = models.TextField(blank=True)
    units = models.CharField(max_length=50, blank=True)
    flag = models.CharField(max_length=10, blank=True)
    notes = models.TextField(blank=True)
