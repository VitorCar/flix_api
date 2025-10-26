from django.db import models
from actors.models import Actors
from genres.models import Genre
from directors.models import Directors


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    director = models.ForeignKey(Directors, on_delete=models.PROTECT, null=True, blank=True, related_name='directors')
    actors = models.ManyToManyField(Actors, related_name='movies')   # ligação n para n
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
