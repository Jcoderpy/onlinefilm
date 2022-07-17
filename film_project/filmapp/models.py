from distutils.command import upload
from django.db import models

# Create your models here.

class Film(models.Model):
    name=models.CharField(max_length=200)
    few=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
