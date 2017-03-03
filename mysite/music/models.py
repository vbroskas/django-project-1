from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=150)
    album_logo = models.CharField(max_length=1000) #for posting a link to an image

    def __str__(self):
        return self.album_title + ' - ' + self.artist  #when we make a call to see what is in the database, thsi will return a user friendly description


class Song(models.Model):
    #each song needs to be associated with its given album
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #create a foreign key based on the primary key of a particular album
    #on_delete=models.CASCADE makes it so whenever an album is deleted, all songs associated with that album are also deleted
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title #print out song title
