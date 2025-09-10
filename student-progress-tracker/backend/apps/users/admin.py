"""
Admin configuration for Users app
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'full_name', 'role', 'is_active']
    list_filter = ['role', 'is_active', 'date_joined']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'full_name', 'phone_number', 'class_name')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
