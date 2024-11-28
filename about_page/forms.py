from django import forms
from .models import RequestNewQuest

class NewQuestForm(forms.ModelForm):
    class Meta:
        model = RequestNewQuest
        fields = ('fname', 'lname', 'email', 'message', 'image')