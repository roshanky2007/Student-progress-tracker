"""
Goals models for Student Progress Tracker
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Add your goals models here
class Goal(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
