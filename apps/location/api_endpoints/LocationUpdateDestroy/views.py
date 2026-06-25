from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, DestroyAPIView

from apps.location.api_endpoints.LocationUpdateDestroy.serializers import LocationUpdateSerializer, LocationDestroySerializer
from apps.location.models import Location

class LocationUpdateAPIView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationUpdateSerializer

class LocationDestroyAPIView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDestroySerializer
