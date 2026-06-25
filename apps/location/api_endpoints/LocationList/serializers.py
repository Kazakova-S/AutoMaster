from rest_framework import serializers
from apps.location.models import Location

class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'