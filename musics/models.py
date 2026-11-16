from django.db import models
from films.models import Movie

# Create your models here.

class Song(models.Model):

    title = models.CharField(max_length=200)

    singers = models.CharField(max_length=200)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    track_no = models.PositiveIntegerField()

    duration = models.FloatField()

    def __str__(self):
        return self.title