from django.shortcuts import render, get_object_or_404, reverse 
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import QuestPost, QuestRecord
from django.views.generic import TemplateView
from .forms import QuestCompletionForm

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'
    
class QuestRecord(generic.ListView):
    model = QuestRecord
    context_object_name = 'quest_record'    
    
class QuestList(generic.ListView):
    model = QuestPost
    template_name = 'quests.html'
    context_object_name = 'quests'
    paginate_by = 6

    
def quest_post(request, slug):
    
    quest = get_object_or_404(QuestPost, slug=slug)
    quest_record = quest.quest_records.all().order_by("tokens_earned").values()
    quest_count = quest.quest_records.count()
    
    if request.method == "POST":
        quest_form = QuestCompletionForm(data=request.POST)
        if quest_form.is_valid():
           run_upload = quest_form.save(commit=False)
           run_upload.runner = request.user 
           run_upload.quest = quest
           run_upload.save()
           messages.add_message(
               request, messages.SUCCESS,
               'Run successfully uploaded!'
           )
           
        return HttpResponseRedirect(reverse('quest_post', args=[slug]))
    else:
        quest_form = QuestCompletionForm()
    
            
    
    return render(
        request,
        "quests/quest_post.html",
        {"quest": quest,
         "quest_record": quest_record,
         "quest_form": quest_form,
         "quest_count": quest_count,
         }
    )
        
    
def record_edit(request, slug, quest_record_id):
    
    if request.method == "POST":
        
        quest = get_object_or_404(QuestPost, slug=slug)
        run_upload = get_object_or_404(QuestRecord, pk=quest_record_id)
        quest_form = QuestCompletionForm(data=request.POST, instance=run_upload)

        if quest_form.is_valid() and run_upload.runner == request.user:
            run_upload = quest_form.save(commit=False)
            run_upload.quest = quest
            run_upload.approved = False
            run_upload.save()
            messages.add_message(request, messages.SUCCESS, 'Run updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating run!')
    
    return HttpResponseRedirect(reverse('quest_post', args=[slug]))