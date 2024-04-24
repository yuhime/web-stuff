from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from .models import HomeSettings
from django.conf import settings
import os
from pathlib import Path
import re

@receiver(post_save, sender=HomeSettings)
def _MDparse(sender, instance: HomeSettings, **kwargs):
    if instance.tracker.previous('file') != instance.file:
        if instance.tracker.previous('file'):
            previous_url = '.'+instance.tracker.previous('file').url
            os.unlink(previous_url)

@receiver(post_delete, sender=HomeSettings)
def M0Dparse(sender, instance, **kwargs):
    os.unlink('.'+instance.tracker.previous('file').url)

@receiver(post_save, sender=HomeSettings)
def MDparse(sender, instance: HomeSettings, **kwargs): 
    print('....................', instance.file, "....................")
    video_id =  re.findall(r'watch\?v=([^\W]+)', instance.video_youtube)
    # https://youtu.be/r27fc3Ylsmw
    alternative_id = re.findall(r'https://youtu.be/([^\W]+)', instance.video_youtube)
    if not video_id:
        if alternative_id:
            autoplay = 1 if (instance.video_autoplay) else 0
            mute = 1 if(instance.video_mute) else 0
            new_video_youtube = 'https://www.youtube.com/embed/'+alternative_id[0]+f'?autoplay={autoplay}&mute={mute}'
            if not instance.video_youtube == new_video_youtube:
                instance.video_youtube = new_video_youtube
                instance.save()
        if re.findall(r'embed', instance.video_youtube):
            vid_id = re.findall(r'https://www.youtube.com/embed/([^\?]+)', instance.video_youtube)
            new_video_youtube = 'https://www.youtube.com/embed/'+vid_id[0]+f'?autoplay={1 if (instance.video_autoplay) else 0}&mute={1 if (instance.video_mute) else 0}'
            if not instance.video_youtube == new_video_youtube:
                instance.video_youtube = new_video_youtube
                instance.save()
    else:
        autoplay = 1 if (instance.video_autoplay) else 0
        mute = 1 if(instance.video_mute) else 0
        new_video_youtube = 'https://www.youtube.com/embed/'+video_id[0]+f'?autoplay={autoplay}&mute={mute}'
        if not instance.video_youtube == new_video_youtube:
            instance.video_youtube = new_video_youtube
            instance.save()