from rest_framework import serializers

from home.models import Sauna


class SaunaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    last_chair_person = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Sauna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.last_chair_person = validated_data.get('last_chair_person', instance.last_chair_person)
        instance.save()
        return instance

    class Meta:
        model = Sauna
        fields = '__all__'