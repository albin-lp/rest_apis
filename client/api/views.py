from django.shortcuts import render
from api.models import Client
from api.serializers import ClientSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Create your views here.

class ClientView(ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def list(self, request, *args, **kwargs):
        cli = Client.objects.all()
        serializer = ClientSerializer(cli, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        cli = Client.objects.get(id=id)
        serializer = ClientSerializer(cli, many=False)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Client.objects.get(id=id)
        serializer = ClientSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        cli = Client.objects.get(id=id)
        holi.delete()
        return Response({"msg": "clienty deleted"})

# Create your views here.
