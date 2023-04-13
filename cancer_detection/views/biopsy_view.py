from django.views.generic import DetailView, CreateView
from cancer_detection.models.sample import Biopsy, MedicalExamination
from cancer_detection.forms.biopsy_form import BiopsyForm


class BiopsyCreate(CreateView):
    model = Biopsy
    form_class = BiopsyForm
    template_name = "biopsy/biopsy_create.html"
    success_url = "/examinations/"

    def form_valid(self, form):
        medical_exam_id = self.kwargs['pk']
        form.instance.medical_examination = MedicalExamination.objects.get(id=medical_exam_id)
        return super().form_valid(form)


class BiopsyDetail(DetailView):
    model = Biopsy
    template_name = "biopsy/biopsy_detail.html"
