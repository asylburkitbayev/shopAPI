from rest_framework.routers import DefaultRouter
from .views import RegistrationSerializerModelViewSet

routers = DefaultRouter()

routers.register('', RegistrationSerializerModelViewSet)

urlpatterns = routers.urls
