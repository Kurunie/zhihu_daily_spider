from django.db import models

# Create your models here.


class Content(models.Model):
    urls = models.CharField(max_length=255)
    urlques = models.CharField(max_length=1000)
    urlans = models.CharField(max_length=10000)
    author = models.CharField(max_length=1000)