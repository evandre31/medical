from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    publication_date = forms.DateTimeInput()

    class Meta:
        model = Patient
        fields = ('nom', 'prenom', 'datedenaissance')


# class PatientForm2(forms.ModelForm):
#     publication_date = forms.DateTimeInput()
#
#     class Meta:
#         model = Fiche
#         fields = ('asa', 'mallampati')
