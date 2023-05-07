
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from hospital.models.department import Department
from hospital.serializers.department import DepartmentSerializer
from utils.pagination import BasePagination


class DepartmentsList(mixins.ListModelMixin, GenericAPIView):
    """

            This api is authenticated permission based,
            Responses all the list of departments

    """
    permission_classes = [IsAuthenticated]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    pagination_class = BasePagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
