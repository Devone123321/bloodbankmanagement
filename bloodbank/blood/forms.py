from django import forms
from .models import Donor, Request

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'age', 'blood_type', 'last_donation']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['recipient_name', 'blood_type', 'quantity_needed', 'request_date']
