from django.urls import path
from . import views

# Define URL patterns for the application
urlpatterns = [
    path('', views.about_me, name='about'),

]
