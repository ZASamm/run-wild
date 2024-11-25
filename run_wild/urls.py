from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('quests/', views.QuestList.as_view(), name='quests'),
    path('quest/<slug:slug>/', views.quest_post, name='quest_post'),
]
