from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Squirrel(models.Model):
    Latitude = models.FloatField(blank=False)
    Longitude= models.FloatField(blank=False)
    Unique_Squirrel_ID = models.CharField(max_length=100,unique=True, blank=False)
    Shift=models.CharField(max_length=100, blank=True)
    Date=models.CharField(max_length=100,blank=True)
    Age=models.CharField(max_length=100, blank=True)
    Primary_Fur_Color=models.CharField(max_length=100, blank=True)
    Location=models.CharField(max_length=100, blank=True)
    Specific_Location=models.CharField(max_length=100, blank=True)
    Running=models.BooleanField(blank=True)
    Chasing=models.BooleanField(blank=True)
    Climbing=models.BooleanField(blank=True)
    Eating=models.BooleanField(blank=True)
    Foraging=models.BooleanField(blank=True)
    Other_Activities=models.CharField(max_length=100, blank=True)
    Kuks=models.BooleanField(blank=True)
    Quaas=models.BooleanField(blank=True)
    Moans=models.BooleanField(blank=True)
    Tail_Flags=models.BooleanField(blank=True)
    Tail_Twitches=models.BooleanField(blank=True)
    Approaches=models.BooleanField(blank=True)
    Indifferent=models.BooleanField(blank=True)
    Runs_From=models.BooleanField(blank=True)