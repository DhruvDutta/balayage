from django.db import models
from django.core.validators import FileExtensionValidator
import pillow_avif
class Home_videos(models.Model):
    video = models.FileField(upload_to='video/',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

class Services(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField()
    info=models.TextField(max_length=250)
