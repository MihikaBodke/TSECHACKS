from django import forms
from .models import *


class SelectPatient(forms.Form):
    patientID = forms.ModelChoiceField(
        queryset=Patient.objects.all(), label='Patient')
