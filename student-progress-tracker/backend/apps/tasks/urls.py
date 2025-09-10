"""
URL patterns for Tasks app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks_view, name='tasks'),
]
