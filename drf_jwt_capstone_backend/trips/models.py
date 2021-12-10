from django.db import models
from django.contrib.auth import get_user_model
diver = get_user_model()
# Create your models here.
class Trips(models.Model):
    diver_pk = models.IntegerField(null=True, blank=True)
    location_pk = models.IntegerField(null=True, blank=True)
    date = models.DateField(max_length=1)
    trip_name = models.CharField(max_length=250)
    checklist_1 = models.BooleanField(default=False)
    checklist_2 = models.BooleanField(default=False)
    checklist_3 = models.BooleanField(default=False)
    checklist_4 = models.BooleanField(default=False)
    checklist_5 = models.BooleanField(default=False)
    checklist_6 = models.BooleanField(default=False)
    checklist_7 = models.BooleanField(default=False)
    checklist_8 = models.BooleanField(default=False)
    checklist_9 = models.BooleanField(default=False)
    checklist_10 = models.BooleanField(default=False)