import django_filters
from .models import Location

class LocationFilter(django_filters.FilterSet):
    # Haydovchi xizmat nomi yozsa, matn ichidan qidiradi (masalan: ?xizmat=motor)
    xizmat = django_filters.CharFilter(field_name='xizmatlar', lookup_expr='icontains')
    
    # Haydovchi manzil yozsa, manzil ichidan qidiradi (masalan: ?manzil=Chilonzor)
    manzil = django_filters.CharFilter(field_name='manzil', lookup_expr='icontains')

    class Meta:
        model = Location
        fields = ['xizmat', 'manzil']