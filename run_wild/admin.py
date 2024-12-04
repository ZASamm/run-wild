from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .models import QuestPost, QuestRecord


# Register your models here.
@admin.register(QuestPost)
class QuestPostAdmin(SummernoteModelAdmin):
    list_display = ("title", "difficulty", "distance", "preview_map")
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)

    def preview_map(self, obj):
        if obj.map_route and obj.map_route.url:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>', obj.map_route.url
            )
        return "No map"

    preview_map.short_description = "Route Map"


@admin.register(QuestRecord)
class QuestRecordAdmin(admin.ModelAdmin):
    list_display = (
        "quest",
        "runner",
        "completion_time",
        "tokens_earned",
        "approved"
        )
    list_filter = (
        "approved",
        "is_personal_best"
        )
    search_fields = [
        "runner__username",
        "quest__title"
        ]
    readonly_fields = (
        "tokens_earned",
        "pace",
        "is_personal_best"
        )
    actions = [
        "approve_records",
        "unapprove_records"
        ]

    def approve_records(self, request, queryset):
        queryset.update(approved=True)

    approve_records.short_description = "Approve selected records"

    def unapprove_records(self, request, queryset):
        queryset.update(approved=False)

    unapprove_records.short_description = "Unapprove selected records"
