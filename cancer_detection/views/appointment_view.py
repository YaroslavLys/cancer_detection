from django.views.generic import ListView
from cancer_detection.models.person import Appointment


class AppointmentList(ListView):
    model = Appointment
    template_name = 'appointment/appointment_list.html'
