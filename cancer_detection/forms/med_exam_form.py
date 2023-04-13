from django import forms
from cancer_detection.models.person import Patient, Oncologist
from cancer_detection.models.sample import MedicalExamination


class MedicalExaminationForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    oncologist = forms.ModelChoiceField(queryset=Oncologist.objects.all())

    class Meta:
        model = MedicalExamination
        fields = ['patient', 'oncologist', 'start_date', 'end_date']
