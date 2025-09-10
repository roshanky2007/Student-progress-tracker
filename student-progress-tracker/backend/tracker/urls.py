"""
URL configuration for Student Progress Tracker project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('', include('apps.users.urls')),

    # App URLs
    path('api/users/', include('apps.users.urls')),
    path('api/subjects/', include('apps.subjects.urls')),
    path('api/tasks/', include('apps.tasks.urls')),
    path('api/attendance/', include('apps.attendance.urls')),
    path('api/goals/', include('apps.goals.urls')),
    path('api/resources/', include('apps.resources.urls')),

    # Django REST Framework browsable API
    path('api-auth/', include('rest_framework.urls')),

    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
