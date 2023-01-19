from rest_framework import serializers
from rest_framework.serializers import ValidationError
from apps.sales.models import Sale, SaleProduct
from apps.products.serializers import ProductSerializer


class ListSaleProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = SaleProduct
        fields = ['id', 'sale', 'product', 'amount', 'total_cost', 'total_cashback']

        extra_kwargs = {
            'total_cost': {'read_only': True},
            'total_cashback': {'read_only': True},
        }


class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = ['id', 'sale', 'product', 'amount', 'total_cost', 'total_cashback']

        extra_kwargs = {
            'total_cost': {'read_only': True},
            'total_cashback': {'read_only': True},
        }

    def save(self, **kwargs):
        sale = self.validated_data['sale']
        if sale.sold:
            raise ValidationError(
                'error', 'Продажа уже совершена, Вы не можете больше добавлять продукты в эту продажу',
            )
        super().save(**kwargs)


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'branch', 'client', 'from_balance', 'sold', 'date', 'final_cost', 'final_cashback']

        extra_kwargs = {
            'date': {'read_only': True},
            'final_cost': {'read_only': True},
            'final_cashback': {'read_only': True},

        }


class ListSaleSerializer(serializers.ModelSerializer):
    product_sale = ListSaleProductSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 'branch', 'client', 'from_balance', 'sold', 'date', 'final_cost', 'final_cashback',
                  'product_sale']

        extra_kwargs = {
            'date': {'read_only': True},
            'final_cost': {'read_only': True},
            'final_cashback': {'read_only': True},

        }
