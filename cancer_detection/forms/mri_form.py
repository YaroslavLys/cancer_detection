from django import forms
from cancer_detection.models.sample import MRI


class MRIForm(forms.ModelForm):
    class Meta:
        model = MRI
        fields = ['date', 'type_of_research', 'image']
