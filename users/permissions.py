# permissions.py

from rest_framework import permissions

from users.models import Doctor, Operator, Patient


class UserBasePermission(permissions.BasePermission):
    def __init__(self, model):
        self.model = model

    def has_permission(self, request, view):
        if self.check_user_type(request.user.id):
            return True

    def has_object_permission(self, request, view, obj):
        if self.check_user_type(request.user.id):
            return True
        return False

    def check_user_type(self, user_id):
        try:
            return self.model.objects.get(id=user_id)
        except self.model.DoesNotExist:
            return None


class DoctorPermissionOnly(UserBasePermission):

    def __init__(self):
        super().__init__(Doctor)


class OperatorPermissionOnly(UserBasePermission):

    def __init__(self):
        super().__init__(Operator)


class PatientPermissionOnly(UserBasePermission):

    def __init__(self):
        super().__init__(Patient)

