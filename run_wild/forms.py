from django import forms
from datetime import timedelta
from .models import QuestRecord


class QuestCompletionForm(forms.ModelForm):
    """
    Form for completing a quest, capturing hours, minutes, and seconds.
    """
    hours = forms.IntegerField(
        min_value=0,
        help_text="Enter the number of hours (0+)."
        )
    minutes = forms.IntegerField(
        min_value=0,
        max_value=59,
        help_text="Enter the number of minutes (0-59)."
        )
    seconds = forms.IntegerField(
        min_value=0,
        max_value=59,
        help_text="Enter the number of seconds (0-59)."
        )

    class Meta:
        model = QuestRecord
        fields = ["hours", "minutes", "seconds"]

    def clean(self):
        """
        Cleans the data and calculates the total completion time.
        
        Returns:
            dict: The cleaned data with the added completion_time field.
        """
        cleaned_data = super().clean()
        hours = cleaned_data.get("hours", 0)
        minutes = cleaned_data.get("minutes", 0)
        seconds = cleaned_data.get("seconds", 0)

        cleaned_data["completion_time"] = timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        )
        return cleaned_data

    def save(self, commit=True):
        """
        Saves the form instance with the calculated completion time.
        
        Args:
            commit (bool): Whether to commit the save to the database.
        
        Returns:
            QuestRecord: The saved quest record instance.
        """
        instance = super().save(commit=False)
        instance.completion_time = self.cleaned_data["completion_time"]
        if commit:
            instance.save()
        return instance
