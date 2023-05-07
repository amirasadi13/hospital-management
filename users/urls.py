from django.urls import path

from users.views import (DoctorDetail, DoctorsList, NurseDetail, NursesList,
                         OperatorDetail, OperatorList, PatientDetail,
                         PatientsList)

app_name = 'users'

urlpatterns = [
    path('operator/', OperatorList.as_view(), name='operators-list'),
    path('operator/<uuid:pk>/', OperatorDetail.as_view(), name='operator-detail'),
    path('nurse/', NursesList.as_view(), name='doctors-list'),
    path('nurse/<uuid:pk>/', NurseDetail.as_view(), name='doctor-detail'),
    path('doctor/', DoctorsList.as_view(), name='doctors-list'),
    path('doctor/<uuid:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    path('patient/', PatientsList.as_view(), name='patients-list'),
    path('patient/<uuid:pk>/', PatientDetail.as_view(), name='patient-detail')
]