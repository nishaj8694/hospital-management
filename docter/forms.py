from .models import DoctorProfile,Department
from django import forms
from django.forms import ModelForm

class doc_form(forms.ModelForm):
    class Meta:
        model=DoctorProfile
        # fields='__all__'
        exclude=['user','email_vr','is_varified','is_available']


class department_form(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'        