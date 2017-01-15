from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Appointment, AppointmentInformation
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):  # AppointmentForm(instance=Appointment实例对象) 创建表单实例，该实例可以直接.save()

    class Meta:
        model = Appointment
        fields = ('appointment_time', 'state', 'appointment_maker')


class UserForm(UserCreationForm):  # 添加email

    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField, 'email': forms.EmailField}


class AppointmentInfoForm(forms.ModelForm):

    class Meta:
        model = AppointmentInformation
        fields = ('subject', 'description', 'email', 'name', 'mobile_number')