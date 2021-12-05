from django.db import models
from django.contrib.auth.models import User


class userInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Song(models.Model):
    SONG_CHOICES = [
        ("Public", "Public"),
        ("Private", "Private"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.CharField(max_length=100,id='noom', null=True)
    audio_name = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='music/', blank=True, null=True)
    audio_type = models.CharField(max_length=20, choices=SONG_CHOICES)
    thumbnail = models.ImageField(upload_to='thumbnail/', default='thumbnail/default.jpg', null=True, blank=True)

    def __str__(self):
        return self.user.username + "  " + self.audio_name
