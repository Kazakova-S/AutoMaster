from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from apps.location.api_endpoints.LocationCreate.serilizers import LocationCreateSerializer
from apps.location.models import Location

class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
