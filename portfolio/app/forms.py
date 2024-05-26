from django import forms
from app .models import *
from django.core.exceptions import ValidationError
from django.utils import timezone

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['startdate']
