from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# from patients.models import Profile
from .models import Patient, Consultation
from .forms import PatientForm, ConsultationForm
from django.http import JsonResponse
from django.template.loader import render_to_string


@login_required
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


@login_required
def patient(request):
    return render(request, 'patient/patient.html')


@login_required
def patient_dossier(request, id):
    storage = messages.get_messages(request)
    patient = Patient.objects.get(id=id)  # get profile qui a user(dans profile) = au user request
    consultation = Consultation.objects.filter(patient_id=id)  # get profile qui a user(dans profile) = au user request
    return render(request, 'patient/patient_dossier.html', {'patient': patient, 'consultation': consultation})


@login_required
def nouvelle_consultaion(request, id):
    patient = Patient.objects.get(id=id)  # patient sur le quel on est positionné
    form = ConsultationForm(request.POST)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.created_by = user
            consultation.patient = patient
            consultation.save()
            messages.success(request, 'consultation ajouté')  # qui sera affiché dans redirect template
            return redirect('patient:patient_dossier', patient.id)
    else:
        form = ConsultationForm()
    return render(request, 'patient/nouvelle_consultation.html', {'patient': patient, 'form': form})


def save_all2(request, id, form, template_name):
    patient = Patient.objects.get(id=id)
    user = request.user
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.created_by = user
            consultation.patient = patient
            form.save()
            data['form_is_valid'] = True
            consultation = Consultation.objects.filter(patient_id=id)
            data['consultation_list'] = render_to_string('patient/consultation_list_2.html',
                                                         {'consultation': consultation, 'patient': patient})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form, 'patient': patient
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def consultation_create(request, id):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
    else:
        form = ConsultationForm()
    return save_all2(request, id, form, 'patient/consultation_create.html')


def consultation_update(request, id, id_consultation):
    consultation = get_object_or_404(Consultation, id=id_consultation)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
    else:
        form = ConsultationForm(instance=consultation)
    return save_all2(request, id, form, 'patient/consultation_update.html')


def consultation_delete(request, id, id_consultation):
    patient = Patient.objects.get(id=id)
    data = dict()
    consultation = get_object_or_404(Consultation, id=id_consultation)
    if request.method == 'POST':
        consultation.delete()
        data['form_is_valid'] = True
        consultation = Consultation.objects.filter(patient_id=id)
        data['consultation_list'] = render_to_string('patient/consultation_list_2.html',
                                                     {'consultation': consultation})
    else:
        context = {'consultation': consultation, 'patient': patient}
        data['html_form'] = render_to_string('patient/consultation_delete.html',
                                             context, request=request)
    return JsonResponse(data)

