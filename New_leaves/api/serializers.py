from api.models import Leaves
from rest_framework import serializers



class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leaves
        fields="__all__"

    def create(self, validated_data):
        return Leaves.objects.create(**validated_data)