from django import forms
from cancer_detection.models.sample import BloodTest


class BloodTestForm(forms.ModelForm):
    class Meta:
        model = BloodTest
        fields = ['date', 'type_of_research', 'result']
