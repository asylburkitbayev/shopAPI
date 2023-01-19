from rest_framework.routers import DefaultRouter
from .views import BranchModelViewSet

routers = DefaultRouter()

routers.register('', BranchModelViewSet)

urlpatterns = routers.urls
