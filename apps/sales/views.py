from rest_framework.viewsets import ModelViewSet
from apps.sales.models import Sale, SaleProduct
from .serializers import SaleSerializer, ListSaleProductSerializer, ListSaleSerializer, SaleProductSerializer


class SaleModelViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListSaleSerializer
        return SaleSerializer


class SaleProductModelViewSet(ModelViewSet):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListSaleProductSerializer
        return SaleProductSerializer
