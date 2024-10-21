from django import forms
from .models import Donor, Request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'age', 'blood_type', 'last_donation', 'contact_number']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['recipient_name', 'blood_type', 'quantity_needed', 'request_date']


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')