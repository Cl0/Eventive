from django.db import models
from users.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField('Category', related_name='events')
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
