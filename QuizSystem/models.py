from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,unique=True)
    university = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email
