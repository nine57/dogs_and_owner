from django.db import models
from django.db.models.fields import DateField

# models here.

class Actor(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    movie         = models.ManyToManyField("Movie", through='Actor_movie')

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'

class Actor_movie(models.Model):
    actor = models.ForeignKey("Actor", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'