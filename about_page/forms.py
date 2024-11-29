from django import forms
from .models import RequestNewQuest

class NewQuestForm(forms.ModelForm):
    class Meta:
        model = RequestNewQuest
        fields = ('fname', 'lname', 'email', 'message', 'image')
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Please provide the Name, short description, distance, elevation gain and max elevation.'}),
        }