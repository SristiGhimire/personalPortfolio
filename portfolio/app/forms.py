from django import forms
from app .models import *
from django.core.exceptions import ValidationError
from django.utils import timezone

class AppointmentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label ="name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
        initial = "Name",
    )

    phone = forms.IntegerField(
    required=True,
    widget=forms.NumberInput(attrs={
        'class':'form-control',
    }),
    initial=0,
)


    startdate = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 
                'type': 'datetime-local'
                }
            ),
            initial = timezone.now()
        )
