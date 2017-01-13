from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import AppointmentForm
# Create your views here.


def index(request):
    return HttpResponse('this page is left to demonstrate the appointment available.'
                        '<br><a href="%s">set appointment</a>' % reverse('appointment:set_appointment'))


def set_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("appointment set!")
    else:
        form = AppointmentForm()
    return render(request, 'appointment/set_appointment.html', {'form':form})