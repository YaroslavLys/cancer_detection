from django.views.generic import DetailView, CreateView
from cancer_detection.models.sample import MRI, MedicalExamination
from cancer_detection.forms.mri_form import MRIForm


class MRICreate(CreateView):
    model = MRI
    form_class = MRIForm
    template_name = "mri/mri_create.html"
    success_url = "/examinations/"

    def form_valid(self, form):
        medical_exam_id = self.kwargs['pk']
        form.instance.medical_examination = MedicalExamination.objects.get(id=medical_exam_id)
        return super().form_valid(form)


class MRIDetail(DetailView):
    model = MRI
    template_name = "mri/mri_detail.html"
