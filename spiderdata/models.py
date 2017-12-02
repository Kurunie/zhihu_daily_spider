from django.db import models

# Create your models here.


class Content(models.Model):
    urls = models.CharField(max_length=255)
    urlques = models.CharField(max_length=1000)
    urlans = models.CharField(max_length=10000)
    author = models.CharField(max_length=1000)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
