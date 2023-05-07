from django.urls import path

from hospital.views.department import DepartmentsList
from hospital.views.doctor_turns import DoctorTurns
from hospital.views.operator_turns import OperatorTurns
from hospital.views.patient_turns import PatientTurns

app_name = 'hospital'

urlpatterns = [
    path('operator/turn/', OperatorTurns.as_view(), name='operator-turn-checked-dates-list'),
    path('doctor/turn/', DoctorTurns.as_view(), name='doctor-turn-checked-dates-list'),
    path('patient/turn/', PatientTurns.as_view(), name='patient-turn-checked-dates-list'),
    path('department/', DepartmentsList.as_view(), name='departmentsList')
]