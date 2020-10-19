from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.patient, name='patient'),
    path('patient/', views.patient_list, name='patient_list'),
    path('patient/create', views.patient_create, name='patient_create'),
    path('patient/<id>/update', views.patient_update, name='patient_update'),
    path('patient/<id>/delete', views.patient_delete, name='patient_delete'),
    path('patient/<id>/', views.patient_dossier, name='patient_dossier'),
    path('patient/<id>/consultation_nouvelle', views.nouvelle_consultaion, name='nouvelle_consultaion'),
    path('patient/<id>/consultation_create', views.consultation_create, name='consultation_create'),
    path('patient/<id>/<id_consultation>/update', views.consultation_update, name='consultation_update'),
    path('patient/<id>/<id_consultation>/delete', views.consultation_delete, name='consultation_delete'),
]
