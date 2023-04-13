from django import forms
from cancer_detection.models.sample import Biopsy


class BiopsyForm(forms.ModelForm):
    class Meta:
        model = Biopsy
        fields = ['date', 'type_of_research', 'report']
