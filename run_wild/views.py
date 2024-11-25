from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import QuestPost
from django.views.generic import TemplateView

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
    
    return render(
        request,
        "quests/quest_post.html",
        {"quest": quest}
    )