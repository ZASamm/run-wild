from django.contrib import admin
from .models import QuestPost, QuestRecord

# Register your models here.
admin.site.register(QuestPost)
admin.site.register(QuestRecord)