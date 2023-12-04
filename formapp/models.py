from typing import Any
from django.db import models
# for authentication token
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#   username = models.CharField(max_length=100)
#   email = models.EmailField(max_length=100)
#   password = models.CharField(max_length=100)
  
#   def __str__(self):
#     return self.username

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
      return self.name
    
