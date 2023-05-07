from django.contrib import admin

from hospital.models.department import Department
from hospital.models.turn_checked_date import TurnCheckedDate

admin.site.register(Department)
admin.site.register(TurnCheckedDate)