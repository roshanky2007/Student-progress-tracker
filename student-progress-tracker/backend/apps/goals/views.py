"""
Goals views for Student Progress Tracker
"""
from django.shortcuts import render
from rest_framework import generics
from .models import Goal

def goals_view(request):
    return render(request, 'goals.html')
