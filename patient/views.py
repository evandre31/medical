from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# from patients.models import Profile
from .models import Patient
from .forms import PatientForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def patient_list(request):
    user = request.user  # si non authenticated redirect to login ou autre page
    # patients = Fiche.objects.all()
    patients = Patient.objects.filter(doctor=user.id)
    context = {
        'patients': patients
    }
    return render(request, 'patient/patient_list.html', context)


def save_all(request, form, template_name):
    user = request.user  # si non authenticated redirect to login ou autre page

    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            obj = form.save(commit=False)  # avant de save
            doctor = User.objects.filter(email=user.email).first()  # set the author depuis patient user
            obj.doctor = doctor
            obj.save()  # save

            form.save()
            data['form_is_valid'] = True
            patients = Patient.objects.filter(doctor=user.id)
            data['patient_list'] = render_to_string('patient/patient_list_2.html', {'patients': patients})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
    else:
        form = PatientForm()
    return save_all(request, form, 'patient/patient_create.html')


def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
    else:
        form = PatientForm(instance=patient)
    return save_all(request, form, 'patient/patient_update.html')


# def patient_delete(request, id):
# #     user = request.user  # si non authenticated redirect to login ou autre page
# #     data = dict()
# #     patient = get_object_or_404(Patient, id=id)
# #     if request.method == "POST":
# #         patient.delete()
# #         data['form_is_valid'] = True
# #         patients = Patient.objects.filter(doctor=user.id)
# #         data['patient_list'] = render_to_string('patient/patient_list_2.html', {'patient': patient})
# #     else:
# #         context = {'patient': patient}
# #         data['html_form'] = render_to_string('patient/patient_delete.html', context, request=request)
# #     return JsonResponse(data)
def patient_delete(request, id):
    user = request.user  # si non authenticated redirect to login ou autre page
    data = dict()
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.delete()
        data['form_is_valid'] = True
        patients = Patient.objects.filter(doctor=user.id)
        data['patient_list'] = render_to_string('patient/patient_list_2.html', {'patients': patients})
    else:
        context = {'patient': patient}
        data['html_form'] = render_to_string('patient/patient_delete.html', context, request=request)
    return JsonResponse(data)


def patient(request):
    return render(request, 'patient/patient.html')


def patient(request):
    return render(request, 'patient/patient.html')
