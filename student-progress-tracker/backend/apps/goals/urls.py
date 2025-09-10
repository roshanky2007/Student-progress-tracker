"""
URL patterns for Goals app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.goals_view, name='goals'),
]
