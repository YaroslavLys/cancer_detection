from django.contrib import admin
from cancer_detection.models.person import Oncologist, Patient, Appointment
from cancer_detection.models.sample import MedicalExamination, Biopsy, MRI, BloodTest

# Register your models here.

admin.site.register(Oncologist)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalExamination)
admin.site.register(MRI)
admin.site.register(Biopsy)
admin.site.register(BloodTest)
