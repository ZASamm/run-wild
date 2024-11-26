from django.shortcuts import render, get_object_or_404, reverse 
from django.views import generic
from .models import QuestPost, QuestRecord
from django.views.generic import TemplateView
from .forms import QuestCompletionForm

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'
    
    
class QuestList(generic.ListView):
    model = QuestPost
    template_name = 'quests.html'
    context_object_name = 'quests'
    paginate_by = 6
    
    
def quest_post(request, slug):
    
    quest = get_object_or_404(QuestPost, slug=slug)
    quest_record = quest.quest_records.all().order_by("tokens_earned").values()
    
    if request.method == "POST":
        quest_form = QuestCompletionForm(data=request.POST)
        if quest_form.is_valid():
           run_upload = quest_form.save(commit=false)
           run_upload.user = request.user 
           run_upload.quest = quest
           run_upload.save()
           messages.add_message(
               request, messages.SUCCESS,
               'Run successfully uploaded!'
           )
           
    quest_form = QuestCompletionForm(data=request.POST)
            
    
    return render(
        request,
        "quests/quest_post.html",
        {"quest": quest,
         "quest_record": quest_record,
         "quest_form": quest_form,
         }
    )