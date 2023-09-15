from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .base import CustomUserManager

# Create your models here.

class ApplicationConfig(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SiteUser(AbstractUser):
    
    objects = CustomUserManager()
    email = models.EmailField(max_length=254)
    age = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.username



class Car(ApplicationConfig):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    year = models.IntegerField()
  

    def __str__(self):
        return self.brand  + '' + self.model
    


