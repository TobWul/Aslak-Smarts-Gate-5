import datetime

from rest_framework import viewsets

from temperatures.models import InsideTemperature
from temperatures.serializers import InsideTemperatureSerializer


class InsideTemperatureViewSet(viewsets.ModelViewSet):
    queryset = InsideTemperature.objects.all()
    serializer_class = InsideTemperatureSerializer
