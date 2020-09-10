from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.patient, name='patient'),
    path('patient/', views.patient_list, name='patient_list'),
    path('patient/create', views.patient_create, name='patient_create'),
    path('patient/(?P<id>\d+)/update', views.patient_update, name='patient_update'),
    path('patient/(?P<id>\d+)/delete', views.patient_delete, name='patient_delete'),
    path('patient/(?P<id>\d+)/', views.patient_dossier, name='patient_dossier'),
    path('patient/(?P<id>\d+)/consultation_nouvelle', views.nouvelle_consultaion, name='nouvelle_consultaion'),
]