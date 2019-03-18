from rest_framework import routers

from components.viewsets import ComponentViewSet
from temperatures.viewsets import InsideTemperatureViewSet
from utilities.viewsets import ElectricityViewSet

router = routers.DefaultRouter()
router.register(r'electricity', ElectricityViewSet)
router.register(r'inside-temperatures', InsideTemperatureViewSet)
