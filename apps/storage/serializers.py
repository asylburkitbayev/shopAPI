from rest_framework import serializers
from .models import Storage, AddProductStorage


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class AddProductStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProductStorage
        fields = '__all__'
