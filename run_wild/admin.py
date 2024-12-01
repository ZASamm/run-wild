from django.contrib import admin
from .models import QuestPost, QuestRecord
from django_summernote.admin import SummernoteModelAdmin

@admin.register(QuestPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(QuestRecord)