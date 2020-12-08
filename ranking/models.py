from django.db import models
from django.conf import settings
from django.utils import timezone

class Film(models.Model):
    IMDb_id = models.CharField(max_length=9, primary_key=True)

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    score = models.PositiveSmallIntegerField(default=0)

    def publish(self):
        self.date = timezone.now()
        self.save()