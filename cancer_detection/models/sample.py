from django.db import models

from cancer_detection.models.person import Patient, Oncologist


class Sample(models.Model):
    date = models.DateField()
    type_of_research = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.type_of_research}"


class MedicalExamination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    oncologist = models.ForeignKey(Oncologist, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"ME |{self.start_date} - {self.end_date}| {self.patient.name} {self.patient.surname} : {self.oncologist.name} {self.oncologist.surname}"


class BloodTest(Sample):
    result = models.TextField(max_length=400)
    medical_examination = models.OneToOneField(MedicalExamination, on_delete=models.CASCADE)


class MRI(Sample):
    image = models.CharField(max_length=150, default="Beautiful image")
    medical_examination = models.OneToOneField(MedicalExamination, on_delete=models.CASCADE)


class Biopsy(Sample):
    report = models.TextField(max_length=400)
    medical_examination = models.OneToOneField(MedicalExamination, on_delete=models.CASCADE)
