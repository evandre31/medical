from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Patient(models.Model):
    nom = models.CharField(max_length=50, null=False, blank=False)
    prenom = models.CharField(max_length=50, null=False, blank=False)
    datedenaissance = models.DateField(verbose_name="date de naissance")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Consultation(models.Model):
    patient = models.ForeignKey(Patient, related_name='consultations', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='consultations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    motif = models.CharField(max_length=250)

    def __str__(self):
        return self.motif
