from django.db import models
from django.contrib.auth import get_user_model
diver = get_user_model()
# Create your models here.
class Replies(models.Model):
    review_pk = models.IntegerField(null=True, blank=True)
    diver_pk = models.ForeignKey(diver, null=True, blank=True, on_delete=models.CASCADE)
    reply = models.CharField(max_length=250)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)