from django.contrib import admin

from users.models import Doctor, Nurse, Operator, Patient, User

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Operator)