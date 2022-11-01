from django.contrib import admin
from .models import Artiste, Song, Lyric

# Register your models here.
# admin.site.register(Artiste)
# admin.site.register(Song)
# admin.site.register(Lyric)

class SongInline(admin.TabularInline):
    model=Song
    fk_name = "artist"
    extra=3

class ArtisteAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['first_name']}),
    ('last name',{'fields':['last_name']}),
    ('age',{'fields':['age'], 'classes':['collapse']}),]
    
    inlines=[
        SongInline ,

    ]
    # inlines:LyricInline


admin.site.register(Artiste, ArtisteAdmin)