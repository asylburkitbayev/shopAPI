from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, ProductModelViewSet, ProductImageModelViewSet, TypeProductModelViewSet

routers = DefaultRouter()

routers.register('categories', CategoryModelViewSet)
routers.register('product_images', ProductImageModelViewSet)
routers.register('products', ProductModelViewSet)
routers.register('type_products', TypeProductModelViewSet)

urlpatterns = routers.urls
