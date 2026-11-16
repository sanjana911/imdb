from django.db import models

# Create your models here.

class Movie(models.Model):

    title = models.CharField(max_length=200)

    director = models.CharField(max_length=100)

    year = models.PositiveIntegerField()

    language = models.CharField(max_length=100)

    GENRE_OPTIONS = (
        ("comedy","comedy"),
        ("thriller","thriller"),
        ("action","action"),
        ("horror","horror"),
        ("romantic","romantic"),
        ("other","other")
    )

    genre = models.CharField(max_length=100, choices= GENRE_OPTIONS)

    duration = models.FloatField()

    def __str__(self):
        return self.title

