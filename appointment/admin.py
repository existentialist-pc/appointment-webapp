from django.contrib import admin
from .models import Appointment
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    fields = ['appointment_time', 'state', 'appointment_maker']
    list_display = ('appointment_time', 'state', 'appointment_maker')
    list_filter = ['state']
    search_fields = ['appointment_time']

admin.site.register(Appointment, AppointmentAdmin)