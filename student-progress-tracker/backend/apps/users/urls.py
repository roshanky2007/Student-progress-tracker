"""
URL patterns for Users app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    # Web views
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    # API views
    path('api/users/', views.UserListAPIView.as_view(), name='api_users'),
]
