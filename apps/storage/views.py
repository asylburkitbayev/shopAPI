from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Storage, AddProductStorage
from .serializers import StorageSerializer, AddProductStorageSerializer


class StorageModelViewSet(ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class AddProductStorageModelViewSet(ModelViewSet):
    queryset = AddProductStorage.objects.all()
    serializer_class = AddProductStorageSerializer
