from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .models import About, RequestNewQuest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing About objects.
    """
    list_display = ('title', 'preview_pic', 'updated_on')
    summernote_fields = ('content',)

    def preview_pic(self, obj):
        """
        Displays a small preview of the profile picture.

        Args:
            obj (About): The About object.

        Returns:
            str: HTML for the image preview or a "No image" message.
        """
        if obj.profile_pic and obj.profile_pic.url:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>',
                obj.profile_pic.url
                )
        return "No image"
    preview_pic.short_description = 'Profile Picture'


@admin.register(RequestNewQuest)
class RequestNewQuestAdmin(admin.ModelAdmin):
    """
    Admin interface for managing RequestNewQuest objects.
    """
    list_display = ('full_name', 'email', 'preview_image', 'read')
    list_filter = ('read',)
    search_fields = ['fname', 'lname', 'email', 'message']
    actions = ['mark_as_read', 'mark_as_unread']

    def full_name(self, obj):
        """
        Concatenates the first name and last name of the requester.

        Args:
            obj (RequestNewQuest): The RequestNewQuest object.

        Returns:
            str: The full name of the requester.
        """
        return f"{obj.fname} {obj.lname}"

    full_name.short_description = 'Name'

    def preview_image(self, obj):
        """
        Displays a small preview of the request image.

        Args:
            obj (RequestNewQuest): The RequestNewQuest object.

        Returns:
            str: HTML for the image preview or a "No image" message.
        """
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>', obj.image.url
                )
        return "No image"
    preview_image.short_description = 'Image'

    def mark_as_read(self, request, queryset):
        """
        Marks the selected quest requests as read.

        Args:
            request: The HTTP request object.
            queryset: The queryset of selected RequestNewQuest objects.
        """
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected requests as read"

    def mark_as_unread(self, request, queryset):
        """
        Marks the selected quest requests as unread.

        Args:
            request: The HTTP request object.
            queryset: The queryset of selected RequestNewQuest objects.
        """
        queryset.update(read=False)
    mark_as_unread.short_description = "Mark selected requests as unread"
