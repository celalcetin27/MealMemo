from django.db import models

class UserImage(models.Model):
    image = models.ImageField('user_images/')
    image_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length = 256)

