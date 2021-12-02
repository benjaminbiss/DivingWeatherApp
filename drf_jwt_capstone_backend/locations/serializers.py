from rest_framework import serializers
from .models import Locations

class LocationSerializer(serializers.ModelSerializer):
    model = Locations
    fields = {'latitude', 'longitude', 'name', 'url'}