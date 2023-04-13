"""software_design_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cancer_detection.views.upload_csv_view import UploadDataCSVFile
from cancer_detection.views.patient_view import PatientDelete, PatientList, PatientDetail
from cancer_detection.views.oncologist_view import OncologistDelete, OncologistList, OncologistDetail
from cancer_detection.views.appointment_view import AppointmentList
from cancer_detection.views.med_exam_view import MedicalExaminationList, MedicalExaminationDetail, \
    MedicalExaminationDelete, MedicalExaminationCreateView, MedicalExaminationUpdate
from cancer_detection.views.blood_test_view import BloodTestCreate, BloodTestDetail
from cancer_detection.views.mri_view import MRIDetail, MRICreate
from cancer_detection.views.biopsy_view import BiopsyDetail, BiopsyCreate

urlpatterns = [
    path('', UploadDataCSVFile.as_view(), name='home'),

    path('admin/', admin.site.urls),

    path('patients/', PatientList.as_view(), name='patient_list'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient_detail'),
    path('patients/<int:pk>/patient_delete/', PatientDelete.as_view(), name='patient_delete'),

    path('oncologists/', OncologistList.as_view(), name='oncologist_list'),
    path('oncologists/<int:pk>/', OncologistDetail.as_view(), name='oncologist_detail'),
    path('oncologists/<int:pk>/oncologist_delete/', OncologistDelete.as_view(), name='oncologist_delete'),

    path('appointments/', AppointmentList.as_view(), name='appointment_list'),

    path('examinations/', MedicalExaminationList.as_view(), name='med_exam_list'),
    path('examinations/<int:pk>/', MedicalExaminationDetail.as_view(), name='med_exam_detail'),
    path('examinations/<int:pk>/examination_delete/', MedicalExaminationDelete.as_view(), name='med_exam_delete'),
    path('examinations/<int:pk>/examination-update', MedicalExaminationUpdate.as_view(), name='med_exam_update'),
    path('examinations/<int:pk>/add-blood-test/', BloodTestCreate.as_view(), name='blood_test_create'),
    path('examinations/<int:pk>/blood-test-detail/', BloodTestDetail.as_view(), name='blood_test_detail'),
    path('examinations/<int:pk>/add-mri/', MRICreate.as_view(), name='mri_create'),
    path('examinations/<int:pk>/mri-detail/', MRIDetail.as_view(), name='mri_detail'),
    path('examinations/<int:pk>/add-biopsy/', BiopsyCreate.as_view(), name='biopsy_create'),
    path('examinations/<int:pk>/biopsy-detail', BiopsyDetail.as_view(), name='biopsy_detail'),
    path('examinations/create', MedicalExaminationCreateView.as_view(), name='med_exam_create'),

]
