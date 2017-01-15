from django.conf.urls import url, include
from . import views


app_name = 'appointment'
urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', views.set_appointment, name='set_appointment'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, name = 'index'),
    url(r'^set_appointment/$', views.set_appointment, name='set_appointment'),
    url(r'^manage/$', views.manage_appointment, name='manage_appointment'),
    url(r'^(?P<appointment_id>[0-9]+)/appointment_info$', views.appointment_info_edit, name='appointment_info_edit'),
    url(r'^appointment_info/(?P<appointment_info_id>[0-9]+)/$', views.appointment_info_applied, name='appointment_info_applied')
]