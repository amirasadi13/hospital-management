from rest_framework import serializers

from hospital.models.turn_checked_date import TurnCheckedDate
from users.serializers import UserBaseInfoSerializer


class TurnCheckedDatesListSerializer(serializers.ModelSerializer):
    doctor = UserBaseInfoSerializer(read_only=True)
    patient = UserBaseInfoSerializer(read_only=True)

    class Meta:
        model = TurnCheckedDate
        fields = '__all__'


class TurnCheckedDateDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TurnCheckedDate
        fields = '__all__'
