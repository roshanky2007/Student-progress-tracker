"""
Admin configuration for Resources app
"""
from django.contrib import admin
from .models import Resource

admin.site.register(Resource)
