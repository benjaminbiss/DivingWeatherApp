from rest_framework import serializers
from .models import Trips

class TripsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trips
        fields = ('id', 'location_pk', 'diver_pk', 'date', 'trip_name', 'checklist_1', 'checklist_2', 'checklist_3', 'checklist_4', 'checklist_5', 'checklist_6', 'checklist_7', 'checklist_8', 'checklist_9', 'checklist_10',)