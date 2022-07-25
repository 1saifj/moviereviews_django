from django.db import models


class Movie (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(max_length=200, blank=True)