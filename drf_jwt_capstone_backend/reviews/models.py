from django.db import models

# Create your models here.
class Reviews(models.Model):
    location_pk = models.IntegerField(null=True, blank=True)
    diver_pk = models.IntegerField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    review = models.CharField(max_length=250)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)