from rest_framework import serializers
from api.models import Client
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


def create(self, validated_data):
    return Client.objects.create(**validated_data)