from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from cancer_detection.models.sample import MedicalExamination, BloodTest, Biopsy, MRI
from cancer_detection.forms.med_exam_form import MedicalExaminationForm


class MedicalExaminationList(ListView):
    model = MedicalExamination
    template_name = 'med_examination/med_examination_list.html'


class MedicalExaminationDetail(DetailView):
    model = MedicalExamination
    template_name = 'med_examination/med_examination_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medical_examination = self.get_object()
        context['bloodtest'] = BloodTest.objects.filter(medical_examination=medical_examination)
        context['mri'] = MRI.objects.filter(medical_examination=medical_examination)
        context['biopsy'] = Biopsy.objects.filter(medical_examination=medical_examination)
        return context


class MedicalExaminationDelete(DeleteView):
    model = MedicalExamination
    success_url = "/examinations/"
    template_name = "med_examination/med_examination_delete.html"


class MedicalExaminationCreateView(CreateView):
    model = MedicalExamination
    form_class = MedicalExaminationForm
    template_name = 'med_examination/med_examination_create.html'
    success_url = '/examinations/'

    def form_valid(self, form):
        med_examination = form.save(commit=False)
        med_examination.patient = form.cleaned_data['patient']
        med_examination.oncologist = form.cleaned_data['oncologist']
        med_examination.save()
        return super().form_valid(form)


class MedicalExaminationUpdate(UpdateView):
    model = MedicalExamination
    form_class = MedicalExaminationForm
    template_name = 'med_examination/med_examination_update.html'
    success_url = '/examinations/'
