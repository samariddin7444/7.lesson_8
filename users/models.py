from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.URLField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Songs(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    last_update = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


