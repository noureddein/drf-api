from email.mime import image
from django.db import models
from django.contrib.auth import get_user_model


class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image_link = models.URLField(max_length=555)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default=1)
