from rest_framework import serializers
from .models import Reviews

class ReviewsSerializer(serializers.ModelSerializer):
    model = Reviews
    fields = {'location_pk', 'diver_pk', 'stars', 'review', 'likes', 'dislikes'}