from django.db import models
from django.db.models.fields import DateField

# models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    lsat_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()