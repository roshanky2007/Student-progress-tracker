"""
Serializers for User app API endpoints
"""
from rest_framework import serializers
from .models import CustomUser, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'full_name', 'role', 'profile_photo', 
                 'phone_number', 'class_name', 'student_id', 'subjects_taught']

class UserProfileSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='user', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user_info', 'address', 'emergency_contact', 'overall_grade',
                 'overall_percentage', 'email_notifications', 'dark_mode']
