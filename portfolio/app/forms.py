from django import forms
from app .models import *


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        widgets = {
            'startdate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'enddate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }