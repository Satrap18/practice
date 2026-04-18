from django.db import models

# Create your models here.
class LoginForms(models.Model):
    
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    passwords = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)

