from xml.sax import default_parser_list
from django.db import models

from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age= models.IntegerField(default=18)

    def __str__(self):
        return self.first_name


class Song(models.Model):
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField('date released')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content=  models.CharField(max_length=350)

    def __str__(self):
        return self.content

# Create your models here.
