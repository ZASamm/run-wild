from django import forms
from datetime import timedelta
from .models import QuestRecord


class QuestCompletionForm(forms.ModelForm):
    hours = forms.IntegerField(min_value=0)
    minutes = forms.IntegerField(min_value=0, max_value=59)
    seconds = forms.IntegerField(min_value=0, max_value=59)

    class Meta:
        model = QuestRecord
        fields = ["hours", "minutes", "seconds"]

    def clean(self):
        cleaned_data = super().clean()
        hours = cleaned_data.get("hours", 0)
        minutes = cleaned_data.get("minutes", 0)
        seconds = cleaned_data.get("seconds", 0)

        cleaned_data["completion_time"] = timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        )
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.completion_time = self.cleaned_data["completion_time"]
        if commit:
            instance.save()
        return instance
