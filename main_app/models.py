from django.db import models

# Create your models here.
class Hike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    length = models.IntegerField()
    elevation = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name