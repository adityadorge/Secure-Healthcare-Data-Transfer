from django.contrib import admin
from .models import Patient, Patient_medical_history, Patient_medication, Patient_allergy, Patient_vaccination, Vaccine, Allergy, Medication
admin.site.register (Patient)
admin.site.register (Patient_medical_history)
admin.site.register (Patient_medication)
admin.site.register (Patient_allergy)
admin.site.register (Patient_vaccination)
admin.site.register (Vaccine)
admin.site.register (Allergy)
admin.site.register (Medication)


