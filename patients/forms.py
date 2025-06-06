from django import forms

class PatientEnrollmentForm(forms.Form):
    patient_id = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = forms.CharField(widget=forms.Textarea)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    fingerprint = forms.FileField()
