from api.models import Project
from rest_framework import serializers



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"

    def create(self, validated_data):
        return Project.objects.create(**validated_data)