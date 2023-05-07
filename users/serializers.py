from rest_framework import serializers

from users.models import User


class UserBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
        read_only_fields = ['is_staff', 'is_superuser']


class OperatorSerializer(UserSerializer):
    pass


class NursesSerializer(UserSerializer):
    pass


# Doctor Serializer
class DoctorSerializer(UserSerializer):
    pass


# Patient Serializer
class PatientSerializer(UserSerializer):
    pass