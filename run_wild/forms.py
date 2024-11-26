from django import forms
from .models import QuestRecord

class QuestCompletionForm(forms.ModelForm):
    completion_time = forms.FloatField(
        label = 'Completion Time (Mins)'
    )
    
    class Meta:
        model = QuestRecord
        felids = ('completion_time')