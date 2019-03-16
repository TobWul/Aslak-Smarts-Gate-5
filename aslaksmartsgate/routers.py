from rest_framework import routers

from utilities.viewsets import ElectricityViewSet

router = routers.DefaultRouter()
router.register(r'electricity', ElectricityViewSet)
