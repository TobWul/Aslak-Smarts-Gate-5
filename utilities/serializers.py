from rest_framework import serializers

from utilities.models import Electricity


class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Electricity
        fields = '__all__'
