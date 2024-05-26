from django import forms
from app .models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = '__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

