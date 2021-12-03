from django.db import models
from django.contrib.auth import get_user, get_user_model
diver = get_user_model()
# Create your models here.
class Reviews(models.Model):
    location_pk = models.IntegerField(null=True, blank=True)
    diver_pk = models.ForeignKey(diver, null=True, blank=True, on_delete=models.CASCADE)
    stars = models.IntegerField(null=True, blank=True)
    review = models.CharField(max_length=250)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)