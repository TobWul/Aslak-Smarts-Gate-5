from rest_framework import viewsets

from components.models import Component
from components.serializers import ComponentSerializer


class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
