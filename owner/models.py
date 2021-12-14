from django.db import models
from django.db.models.fields import PositiveIntegerField

# models here.

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.PositiveIntegerField()

    class Meta:
        db_table = "owners"

class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE)

    class Meta:
        db_table = "dogs"