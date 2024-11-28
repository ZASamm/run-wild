from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import NewQuestForm

# Create your views here.


def about_me(request):
    
    if request.method == "POST":
        new_quest_form = NewQuestForm(data=request.POST)
        if new_quest_form.is_valid():
            new_quest_form.save()
            messages.add_message(request, messages.SUCCESS, "Your new quest has been received! We endeavour to respond as soon as we can.")
        
    about = About.objects.all().order_by('-updated_on').first()
    new_quest_form = NewQuestForm()
    
    return render(
        request,
        "about/about.html",
        {"about": about,
         "new_request_form": new_quest_form,   
        }
    )