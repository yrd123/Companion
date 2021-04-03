from django.db import models

# Create your models here.
from django.db import models
import os,pytz
from django.utils import timezone
from django.conf import settings


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # userName = models.CharField(max_length=255)
    longitude = models.CharField(unique=True)
    latitude = models.FloatField(unique=True)
    # password = models.CharField(max_length=20)
    def __str__(self):
        return self.name
