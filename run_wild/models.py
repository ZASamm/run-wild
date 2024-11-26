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
        return f"{self.title} | distance - {self.distance} km"

class QuestRecord(models.Model):
    runner = models.ForeignKey(User, on_delete=models.CASCADE)
    quest = models.ForeignKey(QuestPost, on_delete=models.CASCADE, related_name='quest_records')
    completion_time = models.FloatField()
    tokens_earned = models.IntegerField()
    completion_date = models.DateTimeField(auto_now_add=True)
    is_personal_best = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        """
        Calculate the tokens based on the quest distance (calculated at 10 tokens per km)
        """
        self.tokens_earned = round(self.quest.distance * 10)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.runner} completed {self.quest.title} | total tokens earned: {self.tokens_earned}"