from django.shortcuts import render, get_object_or_404, reverse 
from django.views import generic
from django.contrib import messages
from django.db.models import Sum, Count
from datetime import timedelta
from django.http import HttpResponseRedirect
from .models import QuestPost, QuestRecord
from django.views.generic import TemplateView
from .forms import QuestCompletionForm

# Create your views here.
class HomePage(generic.ListView):
    """
    Displays home page
    """
    model = QuestPost
    template_name = 'index.html'
    context_object_name = 'quests'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # get all the approved QuestRecord
        approved_records = QuestRecord.objects.filter(approved=True)
        
        
        # calc total kilometer
        total_kilometers = approved_records.aggregate(
            total_km=Sum('quest__distance'))['total_km'] or 0
        
        # Calc total time
        total_time = approved_records.aggregate(
            total_time=Sum('completion_time'))['total_time'] or timedelta()
        
        # Convert timedelta to hours
        total_hours = total_time.total_seconds() / 3600
        
        # Count total approved completions
        total_completions = approved_records.count()
        
        # Add to context
        context.update({
            'total_kilometers': round(total_kilometers, 0),
            'total_hours': round(total_hours, 0),
            'total_completions': total_completions,
        })
        
        return context
           
class QuestRecordList(generic.ListView):
    model = QuestRecord
    context_object_name = 'quest_record'    
    
class QuestList(generic.ListView):
    model = QuestPost
    template_name = 'quests.html'
    context_object_name = 'quests'
    paginate_by = 4

    
def quest_post(request, slug):
    quest = get_object_or_404(QuestPost, slug=slug)
    quest_record = quest.quest_records.all().order_by("-tokens_earned")
    quest_count = quest.quest_records.count()
    
    if request.method == "POST":
        quest_form = QuestCompletionForm(data=request.POST)
        if quest_form.is_valid():
            run_upload = quest_form.save(commit=False)
            run_upload.runner = request.user 
            run_upload.quest = quest
            run_upload.save()
            
            calc = run_upload._calculation_values
            messages.success(
                request,
                f""" 
                <div class='calculation-breakdown'>
                    <h5>Quest Completed Successfully!</h5>
                    <div class='token-details'>
                        <div>Base Tokens: <span>{calc['base_tokens']}</span></div>
                        <div>Pace Bonus: <span>+{calc['pace_tokens']}</span></div>
                        <div>Personal Best Bonus: <span>+{calc['bonus_tokens']}</span></div>
                        <div>Difficulty Multiplier: <span>{calc['multiplier']}x</span></div>
                        <div class='total'>Total Tokens: <span>{run_upload.tokens_earned}</span></div>
                    </div>
                </div>
                """
            )
           
        return HttpResponseRedirect(reverse('quest_post', args=[slug]))

    quest_form = QuestCompletionForm()
    return render(
        request,
        "quests/quest_post.html",
        {
            "quest": quest,
            "quest_record": quest_record,
            "quest_form": quest_form,
            "quest_count": quest_count,
        }
    )

 
 
 # run upload
 
 # adds view for editing run data       

def record_edit(request, slug, quest_record_id):
    quest = get_object_or_404(QuestPost, slug=slug)
    run_upload = get_object_or_404(QuestRecord, pk=quest_record_id) 
    
    if request.method == "POST":
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

# add delete view

def record_delete(request, slug, quest_record_id):
    
    quest = get_object_or_404(QuestPost, slug=slug)
    run_upload = get_object_or_404(QuestRecord, pk=quest_record_id) 
    
    if run_upload.runner == request.user:
        run_upload.delete()
        messages.add_message(request, messages.SUCCESS, 'Run deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own run!')

    return HttpResponseRedirect(reverse('quest_post', args=[slug]))



# Add a view to get run data for editing

def get_run_data(request, quest_record_id):
    run_upload = get_object_or_404(QuestRecord, pk=quest_record_id)
    
    if run_upload.runner != request.user:
        return JsonResponse({'error': 'Not authorized'}, status=403)
        
    data = {
        'completion_time': run_upload.completion_time,
        'tokens_earned': run_upload.tokens_earned,
    }
    
    return JsonResponse(data)