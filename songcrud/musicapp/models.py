from django.db import models

from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age= models.IntegerField


class Song(models.Model):
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField('date released')
    likes = models.IntegerField(default=0)


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content=  models.CharField(max_length=350)

# Create your models here.
