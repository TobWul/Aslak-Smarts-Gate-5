from rest_framework import viewsets

from utilities.models import Electricity
from utilities.serializers import ElectricitySerializer


class ElectricityViewSet(viewsets.ModelViewSet):
    queryset = Electricity.objects.all()
    serializer_class = ElectricitySerializer
