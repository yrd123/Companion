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
    longitude = models.FloatField()
    latitude = models.FloatField()
    speciality = models.CharField(max_length=255)
    # password = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Disease(models.Model):
  disease_name = models.CharField(max_length=255)
  speciality=models.CharField(max_length=255)
  description=models.TextField(max_length=9000, default="No infromation")
  def __str__(self):
    return self.disease_name


    
