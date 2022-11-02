from django.shortcuts import get_object_or_404, render
from .models import Artiste, Song,Lyric
from django.http import HttpResponse

def index(request):
    data=[]
    songs=Song.objects.all()
    
    for song in songs:
        needs={"title": song.title,
                "release_date":song.date_released,
                "likes":song.likes,
                "artist_first_name":song.artist.first_name,
                "artist_last_name":song.artist.last_name,
                }
        data.append(needs)
    return HttpResponse(data)


def getSong(request,id):
    data=[]
    try:
        song=Song.objects.get(pk=id)
        needs={"title": song.title,
                "release_date":song.date_released,
                "likes":song.likes,
                "artist_first_name":song.artist.first_name,
                "artist_last_name":song.artist.last_name,
                }
    except Song.DoesNotExist:
        raise Http404("Artist does not exist")
    data.append(needs)
    return HttpResponse(data)

def deleteSong(request,id):
    song=get_object_or_404(Song,pk=id)
    song.delete()
    return HttpResponse(f"SONG WITH CURRENT ID {id} HAS BEEN DELETED")


def updateSong(request,id):
     song=get_object_or_404(Song,pk=id)
     try:
        song.title = request.form.get('title')
        song.date_released = request.form.get('date_released')
        song.likes = request.form.get('likes')
     except Song.DoesNotExist:
        raise Http404("Artist does not exist")
     song.save()
     return HttpResponse(f"SONG WITH CURRENT ID {id} HAS BEEN UPDATED")

def getArtists(request):
    data=[]
    artists=Artiste.objects.all()
    for artist in artists:
        needs={
                "first_name":artist.first_name,
                "last_name":artist.last_name,
                }
        data.append(needs)
    return HttpResponse(data)




# Create your views here.
