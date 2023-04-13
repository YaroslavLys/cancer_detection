from django.views.generic import ListView, DetailView, DeleteView
from cancer_detection.models.person import Patient


class PatientList(ListView):
    model = Patient
    template_name = 'patient/patient_list.html'


class PatientDetail(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'


class PatientDelete(DeleteView):
    model = Patient
    success_url = "/patients/"
    template_name = "patient/patient_delete.html"
