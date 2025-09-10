"""
Tasks views for Student Progress Tracker
"""
from django.shortcuts import render
from rest_framework import generics
from .models import Task

def tasks_view(request):
    return render(request, 'tasks.html')
