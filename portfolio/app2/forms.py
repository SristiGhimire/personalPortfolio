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
    

