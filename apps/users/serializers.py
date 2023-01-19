from rest_framework import serializers
from .models import User, CustomUserManager


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'qr_code', 'password', 'is_active', 'is_seller', 'cashback_all']

        extra_kwargs = {
            'qr_code': {'read_only': True},
            'email': {'required': True},
            'is_active': {'read_only': True},
            'is_seller': {'read_only': True},
            'cashback_all': {'read_only': True}
        }

