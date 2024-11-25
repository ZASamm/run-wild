from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# class User(AbstractUser):
#     total_tokens = models.IntegerField(default=0)

class QuestPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=False)
    description = models.CharField(max_length=400)
    difficulty = models.CharField(max_length=200)
    map_route = CloudinaryField('image', default='placeholder')
    distance = models.FloatField()
    elevation_max = models.IntegerField()
    elevation_gain = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} | distance - {self.distance} KM"

