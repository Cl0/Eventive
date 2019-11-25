from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  '''events = models.OneToMany(Event)'''
  firstname = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
     
  # add additional fields in here

  def __str__(self):
    return self.username
