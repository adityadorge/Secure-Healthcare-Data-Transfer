from django.contrib import admin
from .models import Patient, Patient_medical_history, Patient_medication, Patient_disease, Patient_vaccination, Vaccine, Disease, Medication
admin.site.register (Patient)
admin.site.register (Patient_medical_history)
admin.site.register (Patient_medication)
admin.site.register (Patient_disease)
admin.site.register (Patient_vaccination)
admin.site.register (Vaccine)
admin.site.register (Disease)
admin.site.register (Medication)


