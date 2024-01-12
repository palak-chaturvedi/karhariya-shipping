from django.utils import timezone

from django.db import models
from django.core import validators

# Create your models here.

class Quotation(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Pol = models.CharField(max_length=25)
    Por = models.CharField(max_length=25)
    Pod = models.CharField(max_length=25)
    FPod = models.CharField(max_length=25)
    Weight = models.FloatField(max_length=25)
    CBM = models.CharField(max_length=25)
    Volume = models.FloatField(max_length=25)
    Hazard = models.CharField(max_length=25)
    Stackable = models.CharField(max_length=25)


class Track(models.Model):
    RO = models.CharField(max_length=20, default="")
    HBL = models.CharField(max_length=20, default="")
    MBL = models.CharField(max_length=20, default="")
    AWB = models.CharField(max_length=20, default="")
    GIGM = models.CharField(max_length=20, default="")
    GIGMDate = models.CharField(max_length=20, default="")
    GIGM = models.CharField(max_length=20, default="")
    CIGMDate = models.CharField(max_length=20, default="")
    FC = models.CharField(max_length=10, default="")
    Details = models.CharField(max_length=1000, default="")
    LastUpdate = models.DateTimeField(default=timezone.now)


