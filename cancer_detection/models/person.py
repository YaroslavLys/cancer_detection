from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        abstract = True


class Oncologist(Person):
    salary = models.DecimalField(max_digits=100, decimal_places=2)


class Patient(Person):
    address = models.CharField(max_length=100)


class Appointment(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    oncologist = models.ForeignKey(Oncologist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name} {self.patient.surname} : {self.oncologist.name} {self.oncologist.surname} | {self.date}"
