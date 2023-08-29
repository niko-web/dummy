from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField(max_length=3)
    
    def __str__(self):
        return self.username



class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.brand   
    


