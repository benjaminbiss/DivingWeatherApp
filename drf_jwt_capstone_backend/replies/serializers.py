from rest_framework import serializers
from .models import Replies

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ('review_pk', 'diver_pk', 'reply', 'likes', 'dislikes')