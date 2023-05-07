from rest_framework.permissions import IsAuthenticated

from hospital.views.utils.user_turns_base_view import UserTurnsBaseView
from users.permissions import DoctorPermissionOnly

"""

        This api is doctor permission based,
        Responses all the list of Patient's booked turns

"""


class DoctorTurns(UserTurnsBaseView):
    permission_classes = [DoctorPermissionOnly, IsAuthenticated]

    # TODO customize orm
    def get_queryset(self):
        return self.model.objects.filter(doctor=self.request.user)
