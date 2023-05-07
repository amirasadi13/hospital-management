from rest_framework.permissions import IsAuthenticated

from hospital.views.utils.user_turns_base_view import UserTurnsBaseView
from users.permissions import OperatorPermissionOnly

"""

    This api is operator permission based,
    Responses all the list of Patient's booked turns

"""


class OperatorTurns(UserTurnsBaseView):
    permission_classes = [OperatorPermissionOnly, IsAuthenticated]

    # TODO customize orm
    def get_queryset(self):
        return self.model.objects.all()
