from rest_framework import serializers
from .models import Reviews

class ReviewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reviews
        fields = {'location_pk', 'diver_pk', 'stars', 'review', 'likes', 'dislikes'}