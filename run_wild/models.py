from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from cloudinary.models import CloudinaryField

# Create your models here.

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
    completion_time = models.DurationField()
    tokens_earned = models.IntegerField()
    completion_date = models.DateTimeField(auto_now_add=True)
    pace = models.FloatField(help_text='Minutes per kilometer', null=True)
    is_personal_best = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        """
        Calculate the total tokens for a challange earned
        - base token (10 per km)
        - personal best bonus
        - pace bonus
        - difficulty multiplier
        """
        
        # personal best checker before saving
        if not self.pk:
            pervious_best = QuestRecord.objects.filter(
                runner=self.runner,
                quest=self.quest,
                approved=True
            ).order_by('completion_time').first()

            if pervious_best:
                self.is_personal_best = self.completion_time < pervious_best.completion_time
                if self.is_personal_best:
                    QuestRecord.objects.filter(
                        runner=self.runner,
                        quest=self.quest,
                        is_personal_best=True
                    ).update(is_personal_best=False)
                    
            else:
                self.is_personal_best = True
                
        
        # calculate base
        base_tokens = round(self.quest.distance * 10)
       
        # caculate pace
        completion_minutes = self.completion_time.total_seconds() / 60
        self.pace = completion_minutes / self.quest.distance
        
        bonus_tokens = 0
        pace_tokens = 0
        
        # caculate pace bouns
        if self.pace < 4:
            pace_tokens = int(self.quest.distance * 15)
        elif self.pace < 5:
            pace_tokens = int(self.quest.distance * 10)
        elif self.pace < 6:
            pace_bonus = int(self.quest.distance * 5)
        elif self.pace < 7:
            pace_bonus = int(self.quest.distance * 2)
        
        # add personal best bonus if true
        if self.is_personal_best:
            bonus_tokens += 5
           
        # define difficulty mulitper    
        difficulty_multipliers = {
            'easy': 1.0,
            'medium': 1.1,
            'hard': 1.2,
        }
        
        multiplier = difficulty_multipliers.get(
            self.quest.difficulty.lower(), 
            1.0
        )
        print(pace_tokens)
        print(bonus_tokens)
        print(multiplier)
        print(base_tokens)
        
        # calculate final tokens    
        self.tokens_earned = round((base_tokens + pace_tokens + bonus_tokens) * multiplier)
        
        # call the orignal save method
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.runner} completed {self.quest.title} | total tokens earned: {self.tokens_earned}"