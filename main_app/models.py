from django.db import models
from django.urls import reverse

# Create your models here.
class Hike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    length = models.IntegerField()
    elevation = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'hike_id': self.id})
    