from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .models import About, RequestNewQuest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'preview_pic', 'updated_on')
    summernote_fields = ('content',)

    def preview_pic(self, obj):
        if obj.profile_pic and obj.profile_pic.url:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>',
                obj.profile_pic.url
                )
        return "No image"
    preview_pic.short_description = 'Profile Picture'


@admin.register(RequestNewQuest)
class RequestNewQuestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'preview_image', 'read')
    list_filter = ('read',)
    search_fields = ['fname', 'lname', 'email', 'message']
    actions = ['mark_as_read', 'mark_as_unread']

    def full_name(self, obj):
        return f"{obj.fname} {obj.lname}"

    full_name.short_description = 'Name'

    def preview_image(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>', obj.image.url
                )
        return "No image"
    preview_image.short_description = 'Image'

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected requests as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
    mark_as_unread.short_description = "Mark selected requests as unread"
