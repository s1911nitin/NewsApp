
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    post_image = models.ImageField(upload_to='postimages',blank=True,null=True)


    def postimage(self):
        try:
            if self.post_image:
                return self.post_image.url
            else:
                return ""
        except Exception as e:
            return e