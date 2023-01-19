from rest_framework.routers import DefaultRouter
from .views import SaleModelViewSet, SaleProductModelViewSet

routers = DefaultRouter()

routers.register('sale', SaleModelViewSet)
routers.register('sale_product', SaleProductModelViewSet)

urlpatterns = routers.urls
