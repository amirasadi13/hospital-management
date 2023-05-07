from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from hospital.models.turn_checked_date import TurnCheckedDate
from hospital.serializers.user_turns import TurnCheckedDatesListSerializer, TurnCheckedDateDetailSerializer
from utils.pagination import BasePagination

"""
    
    Use UserTurnsBaseView for handling the request type , it has effect on serializer 

"""


class UserTurnsBaseView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    pagination_class = BasePagination
    model = TurnCheckedDate

    def get_queryset(self):
        pass

    # Handled Serializers By Request Method
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TurnCheckedDatesListSerializer
        return TurnCheckedDateDetailSerializer

    # Passed Request To Serializer's Create For Defining The Object's Doctor
    def get_serializer_context(self):
        return {'request': self.request}

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

