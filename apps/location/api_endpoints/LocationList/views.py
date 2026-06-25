from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination # Standart pagination

from apps.location.models import Location
from apps.location.api_endpoints.LocationList.serializers import LocationListSerializer
from apps.location.filters import LocationFilter

class LocationListView(ListAPIView):
    # Bazadagi barcha ustaxonalarni olish
    queryset = Location.objects.all()
    
    # Ustaxona serializerini ulaymiz
    serializer_class = LocationListSerializer
    
    # Sahifalarga bo'lib ko'rsatish (Pagination)
    pagination_class = LimitOffsetPagination 
    
    # Filtr tizimini ulash
    filter_backends = [DjangoFilterBackend]
    filterset_class = LocationFilter