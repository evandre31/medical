from django import forms
from .models import Patient, Consultation


class PatientForm(forms.ModelForm):
    publication_date = forms.DateTimeInput()

    class Meta:
        model = Patient
        fields = ('nom', 'prenom', 'datedenaissance')


class ConsultationForm(forms.ModelForm):
    intervention_date = forms.DateTimeInput()

    class Meta:
        model = Consultation
        fields = ('intervention', 'asa', 'mallampati', 'intervention_date')
