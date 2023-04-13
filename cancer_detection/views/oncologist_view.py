from django.views.generic import ListView, DetailView, DeleteView
from cancer_detection.models.person import Oncologist


class OncologistList(ListView):
    model = Oncologist
    template_name = 'oncologist/oncologist_list.html'


class OncologistDetail(DetailView):
    model = Oncologist
    template_name = 'oncologist/oncologist_detail.html'


class OncologistDelete(DeleteView):
    model = Oncologist
    success_url = "/oncologists/"
    template_name = 'oncologist/oncologist_delete.html'
