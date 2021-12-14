"""
Definition of models.
"""

from django.db import models

class Playlist(models.Model):
    url = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")
    name2 = models.CharField(max_length=200, default="")

class Channel(models.Model):
    url = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")
    name2 = models.CharField(max_length=200, default="")

class Watch(models.Model):
    url = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")
    name2 = models.CharField(max_length=200, default="")
