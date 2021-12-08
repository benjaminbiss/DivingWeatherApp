from rest_framework import serializers
from .models import Users

class TripsSerializer(serializers.ModelSerializer):
    model = Users
    fields = {}