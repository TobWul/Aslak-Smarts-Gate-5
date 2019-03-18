from rest_framework import serializers

from components.models import Component, TYPES


class ComponentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=300)
    type = serializers.ChoiceField(required=True, choices=TYPES)
    state = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `Component` instance, given the validated data.
        """
        return Component.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Component` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance

    class Meta:
        model = Component
        fields = '__all__'