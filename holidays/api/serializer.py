from rest_framework import serializers
from api.models import Holiday



class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = "__all__"


def create(self, validated_data):
    return Holiday.objects.create(**validated_data)