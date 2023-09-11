from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class SiteUser(AbstractUser):
    email = models.EmailField(max_length=254)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username



class Car(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand  + '' + self.model
    


