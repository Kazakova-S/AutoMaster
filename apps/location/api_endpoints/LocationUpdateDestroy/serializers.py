from rest_framework import serializers
from apps.location.models import Location

class LocationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class LocationDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

