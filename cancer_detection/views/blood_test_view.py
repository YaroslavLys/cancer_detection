from django.views.generic import DetailView, CreateView
from cancer_detection.models.sample import BloodTest, MedicalExamination
from cancer_detection.forms.blood_test_form import BloodTestForm


class BloodTestCreate(CreateView):
    model = BloodTest
    form_class = BloodTestForm
    template_name = "blood_test/blood_test_create.html"
    success_url = "/examinations/"

    def form_valid(self, form):
        medical_exam_id = self.kwargs['pk']
        form.instance.medical_examination = MedicalExamination.objects.get(id=medical_exam_id)
        return super().form_valid(form)


class BloodTestDetail(DetailView):
    model = BloodTest
    template_name = "blood_test/blood_test_detail.html"
