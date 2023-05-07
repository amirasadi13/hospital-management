from rest_framework.permissions import IsAuthenticated

from hospital.views.utils.user_turns_base_view import UserTurnsBaseView
from users.permissions import PatientPermissionOnly

"""

        This api is patient permission based,
        Responses all the list of Patient's booked turns

"""


class PatientTurns(UserTurnsBaseView):
    permission_classes = [PatientPermissionOnly, IsAuthenticated]

    # TODO customize orm
    def get_queryset(self):
        return self.model.objects.filter(patient=self.request.user)