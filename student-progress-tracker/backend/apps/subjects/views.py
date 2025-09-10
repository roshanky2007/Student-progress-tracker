"""
Subjects views for Student Progress Tracker
"""
from django.shortcuts import render
from rest_framework import generics
from .models import Subject

def subjects_view(request):
    return render(request, 'subjects.html')
