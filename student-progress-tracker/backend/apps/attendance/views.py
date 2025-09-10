"""
Attendance views for Student Progress Tracker
"""
from django.shortcuts import render
from rest_framework import generics
from .models import Attendance

def attendance_view(request):
    return render(request, 'attendance.html')
