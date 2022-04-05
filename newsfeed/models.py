from distutils.command.upload import upload
from django.db import models

# Create your models here.

class News(models.Model):
    headline_number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    news_image = models.ImageField(upload_to='newsimage')



