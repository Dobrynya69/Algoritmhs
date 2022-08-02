from pyexpat import model
from statistics import mode
from django.db import models

class Algorithm(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) :
        return self.name