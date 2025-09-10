"""
User views for Student Progress Tracker
Authentication, registration, and user management
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CustomUser, UserProfile
from .serializers import UserSerializer, UserProfileSerializer


def home_view(request):
    """Home page - redirect based on authentication"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'login.html')

def login_view(request):
    """Custom login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.full_name}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')

def signup_view(request):
    """Student registration view"""
    if request.method == 'POST':
        data = request.POST

        if CustomUser.objects.filter(email=data.get('email')).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')

        if data.get('password') != data.get('confirm_password'):
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        user = CustomUser.objects.create_user(
            username=data.get('email'),
            email=data.get('email'),
            password=data.get('password'),
            full_name=data.get('full_name'),
            role='STUDENT',
            class_name=data.get('class_name'),
            phone_number=data.get('phone_number', ''),
        )

        UserProfile.objects.create(user=user)
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')

    return render(request, 'signup.html')

@login_required
def dashboard_view(request):
    """Main dashboard with role-specific content"""
    context = {'user': request.user}
    return render(request, 'dashboard.html', context)

def logout_view(request):
    """Logout and redirect to home"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# API Views
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.all()
