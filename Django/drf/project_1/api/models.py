from django.db import models

# Create your models here.
class UserProfile(models.Model):
    
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    bio = models.TextField()
    email = models.EmailField(max_length=254)
    
    def __str__(self) -> str:
        return self.name