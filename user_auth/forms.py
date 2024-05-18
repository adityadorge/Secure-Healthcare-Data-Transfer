# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    class Meta:
        model = User
        fields = ('email','name','role')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

# class UserDetailsForm(forms.ModelForm):
#     date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
#     name = forms.CharField(max_length=100)
    
#     class Meta:
#         model = UserDetail
#         fields = ('phone_number', 'date_of_birth', 'city', 'state','profile_picture')
#         labels={'profile_picture':""}