from django.db import models

# Create your models here.
class Movie(models.Model):
    posterURL = models.TextField(default="https://i.namu.wiki/i/BIl3oY17WExT8MRfFK8BAd_OrbuAe6dbY4ouievj5wKjZN5vZqeYF0oGRo37UEnqmRAr4cOxer2xVR7VoMAvgw.webp")
    title = models.TextField()
    releasedYear = models.IntegerField()
    genre = models.TextField()
    stars = models.TextField()
    runningTime = models.IntegerField()
    comments = models.TextField()
    director = models.TextField()
    actors = models.TextField()

    def __str__(self):
        return self.title