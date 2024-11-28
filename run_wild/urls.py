from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('quest-records/', views.QuestRecordList.as_view(), name='quest_records'),
    path('quests/', views.QuestList.as_view(), name='quests'),
    path('quest/<slug:slug>/', views.quest_post, name='quest_post'),
    path('quest/<slug:slug>/edit/<int:quest_record_id>/', 
        views.record_edit, name='record_edit'),
    path('get-run-data/<int:quest_record_id>/', 
        views.get_run_data, name='get_run_data'),
    path('quest/<slug:slug>/delete/<int:quest_record_id>/',
        views.record_delete, name='record_delete'),
]
