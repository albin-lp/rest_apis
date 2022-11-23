from api.models import Employe
from rest_framework import serializers


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields="__all__"

    def create(self, validated_data):
        return Employe.objects.create(**validated_data)