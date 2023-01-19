from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationSerializer
from .models import User


class RegistrationSerializerModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data,
                                            context={'request': request})
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            return Response({'message': 'Пользователь с такой почтой уже существует'},
                            status=status.HTTP_409_CONFLICT)
        if serializer.is_valid():
            account = serializer.save()
            data = serializer.data
            data['response'] = 'Новый пользователь успешно зарегистрирован'
            data['token'] = Token.objects.get(user=account).key
            data['is_active'] = account.is_active
            return Response(data)
        return Response(serializer.errors)
