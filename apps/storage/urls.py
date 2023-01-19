from rest_framework.routers import DefaultRouter
from .views import StorageModelViewSet, AddProductStorageModelViewSet
routers = DefaultRouter()

routers.register('storage', StorageModelViewSet)
routers.register('add_product_storage', AddProductStorageModelViewSet)


urlpatterns = routers.urls
