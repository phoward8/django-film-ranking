from django.db import models
from django.conf import settings
from django.utils import timezone

class Film(models.Model):
    IMDb_id = models.CharField()

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    previous = models.OneToOneField('self', null=True, blank=True, related_name="next")

    def publish(self):
        self.date = timezone.now()
        self.save()