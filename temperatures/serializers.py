from rest_framework import serializers

from temperatures.models import InsideTemperature


class InsideTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsideTemperature
        fields = '__all__'
