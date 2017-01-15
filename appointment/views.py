from django.shortcuts import render, render_to_response  # 不用传递request
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import AppointmentForm, UserForm, AppointmentInfoForm
from .models import Appointment, AppointmentInformation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    appointments = Appointment.objects.filter(state=1)
    return render_to_response('appointment/index.html', {'appointments':appointments})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('appointment:login'))
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form':form})


def edit_profile(request):
    return HttpResponseRedirect(reverse('appointment:manage_appointment'))


@login_required
def set_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('appointment:manage_appointment'))
    else:
        form = AppointmentForm()
    return render(request, 'appointment/set_appointment.html', {'form':form})


@login_required
def manage_appointment(request):  # paginate
    appointments = Appointment.objects.filter(appointment_maker=request.user)
    return render_to_response('appointment/manage.html', {'appointments':appointments})


@login_required
def appointment_info_edit(request, appointment_id):
    if request.method == 'POST':
        form = AppointmentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.appointment_information = form.instance
            appointment.appointment_participant = request.user
            appointment.state = 2
            appointment.save()
            return HttpResponseRedirect(reverse('appointment:index'))
    else:
        form = AppointmentInfoForm()
    return render_to_response('appointment/appointment_info_edit.html', {'form':form, 'appointment_id':appointment_id})


def appointment_info_applied(request, appointment_info_id):
    appointment_info = AppointmentInformation.objects.get(id=appointment_info_id)
    return render_to_response('appointment/appointment_info_applied.html', {'appointment_info':appointment_info})


def manage_appointment_applied(request):
    pass