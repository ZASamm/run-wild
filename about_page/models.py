from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    profile_pic = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title


class RequestNewQuest(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"New quest request from {self.fname} {self.lname}"