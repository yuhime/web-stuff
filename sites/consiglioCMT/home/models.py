from django.db import models
from model_utils import FieldTracker, managers

# Create your models here.
class HomeSettings(models.Model):
    video_youtube = models.CharField(max_length=4090, help_text='Link supported: <br>    · https://www.youtube.com/watch={id} <br>    · https://www.youtu.be/{id}')
    video_autoplay = models.BooleanField(default=True)
    video_mute = models.BooleanField(default=True)
    data_ultimo_consiglio = models.CharField(max_length=90)
    titolo_file = models.CharField(max_length=250)
    file = models.FileField()
    tracker = FieldTracker()

    def __str__(self):
        return 'Home Settings'