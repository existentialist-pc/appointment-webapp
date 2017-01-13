from django.forms import ModelForm
from .models import Appointment


class AppointmentForm(ModelForm):  # AppointmentForm(instance=Appointment实例对象) 创建表单实例，该实例可以直接.save()

    class Meta:
        model = Appointment
        fields = ['appointment_time', 'state', 'appointment_maker']
