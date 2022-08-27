from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=200)
    def __str__(self):
        return self.album_name
class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    def __str__(self):
        return self.artist_name
class Songs(models.Model):
    song_name = models.CharField(max_length=60)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_name