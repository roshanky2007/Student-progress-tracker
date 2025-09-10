"""
Resources views for Student Progress Tracker
"""
from django.shortcuts import render
from rest_framework import generics
from .models import Resource

def resources_view(request):
    return render(request, 'resources.html')
