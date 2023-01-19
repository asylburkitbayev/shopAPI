from rest_framework import serializers
from .models import Branch
from apps.products.serializers import CategorySerializer


class ListBranchSerializer(serializers.ModelSerializer):
    list_categories = CategorySerializer(many=True)

    class Meta:
        model = Branch
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
