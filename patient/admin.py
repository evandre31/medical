from django.contrib import admin

from .models import Patient, Consultation

admin.site.register(Patient)
admin.site.register(Consultation)
