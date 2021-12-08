from django.db import models

# Create your models here.
class Locations(models.Model):
    latitude = models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=8)
    longitude = models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=8)
    name = models.CharField(max_length=50)