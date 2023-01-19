from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, ProductImage, TypeProduct
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, TypeProductSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageModelViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class TypeProductModelViewSet(ModelViewSet):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductSerializer
