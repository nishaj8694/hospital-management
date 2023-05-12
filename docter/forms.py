from .models import DoctorProfile
from django import forms
from django.forms import ModelForm

class doc_form(forms.ModelForm):
    class Meta:
        model=DoctorProfile
        # fields='__all__'
        exclude=['user','email_vr','is_varified','is_available']