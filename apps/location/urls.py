from django.urls import path

from apps.location.api_endpoints.LocationList.views import LocationListView
from apps.location.api_endpoints.LocationCreate.views import LocationCreateAPIView
from apps.location.api_endpoints.LocationUpdateDestroy.views import LocationUpdateAPIView, LocationDestroyAPIView



urlpatterns = [
    path('', LocationListView.as_view(), name='list-location'),
    path('create/', LocationCreateAPIView.as_view(), name='create-location'),
    path('update/', LocationUpdateAPIView.as_view(), name='update-location'),
    path('delete/', LocationDestroyAPIView.as_view(), name='delete-location'),
]