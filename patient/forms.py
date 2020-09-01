from django import forms
from django.forms import TextInput

from .models import Patient, Consultation


class DateInput(forms.DateInput):   # input date avec calendrier
    input_type = 'date'  # input date avec calendrier


class PatientForm(forms.ModelForm):
    datedenaissance = forms.DateField(widget=DateInput(attrs={'placeholder': 'ta date de naissance'}), help_text='dateeee')
    nom = forms.CharField(widget=TextInput(attrs={'placeholder': 'nammmm'}), help_text='nomm')
    prenom = forms.CharField(widget=TextInput(attrs={'placeholder': 'prenom'}), help_text='prenom')

    class Meta:
        model = Patient
        fields = ('nom', 'prenom', 'datedenaissance')


class ConsultationForm(forms.ModelForm):
    intervention_date = forms.DateField(widget=DateInput, help_text='date de lintervention')

    class Meta:
        model = Consultation
        fields = ('intervention', 'asa', 'mallampati', 'intervention_date')
