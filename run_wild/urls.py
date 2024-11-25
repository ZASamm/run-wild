from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('quests/', views.QuestList.as_view(), name='quests'),
]
