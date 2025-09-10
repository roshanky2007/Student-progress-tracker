"""
URL patterns for Subjects app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.subjects_view, name='subjects'),
]
