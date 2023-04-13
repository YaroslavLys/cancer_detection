import datetime

from django.shortcuts import render
from django.views.generic import View
from cancer_detection.models.person import Patient, Oncologist, Appointment
import csv
import random


class UploadDataCSVFile(View):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        csv_file = request.FILES['csv_file']
        csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
        for index, record in enumerate(csv_data):
            if index <= 995:
                upload_patient(record)
            elif index >= 995:
                upload_oncologist(record)

        for _ in range(20):
            upload_appointment()
        return render(request, self.template_name)


def upload_patient(record):
    patient = Patient(name=record[0],
                      surname=record[1],
                      email=record[2],
                      age=record[3],
                      address=record[4])
    patient.save()


def upload_oncologist(record):
    oncologist = Oncologist(name=record[0],
                            surname=record[1],
                            email=record[2],
                            age=record[3],
                            salary=record[4])
    oncologist.save()


def upload_appointment():
    patients = Patient.objects.all()
    oncologists = Oncologist.objects.all()
    appointment = Appointment(date=datetime.date.today(),
                              patient=random.choice(patients),
                              oncologist=random.choice(oncologists))
    appointment.save()
