from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.FileField(upload_to="media/", blank=False, max_length=100)
   
