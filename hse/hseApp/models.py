from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=50)
    pwd = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.userName

class Lois(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.DateField()
    section = models.CharField(max_length=255)

    def __str__(self):
        return self.name
