from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    releasedYear = models.IntegerField()
    genre = models.TextField()
    stars = models.IntegerField()
    runningTime = models.IntegerField()
    comments = models.TextField()
    director = models.TextField()
    actors = models.TextField()

    def __str__(self):
        return self.title