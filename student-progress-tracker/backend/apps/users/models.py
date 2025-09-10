"""
User models for Student Progress Tracker
Custom User model with role-based authentication (Student, Teacher, Parent)
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    """
    Custom User Model extending Django's AbstractUser
    Supports role-based access: Student, Teacher, Parent
    """

    ROLE_CHOICES = [
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
        ('PARENT', 'Parent'),
        ('ADMIN', 'Admin'),
    ]

    CLASS_CHOICES = [
        ('9A', 'Class 9-A'),
        ('9B', 'Class 9-B'),
        ('10A', 'Class 10-A'),
        ('10B', 'Class 10-B'),
        ('11A', 'Class 11-A (Science)'),
        ('11B', 'Class 11-B (Commerce)'),
        ('12A', 'Class 12-A (Science)'),
        ('12B', 'Class 12-B (Commerce)'),
    ]

    # Core fields
    email = models.EmailField(unique=True, help_text="Email address for login")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
    full_name = models.CharField(max_length=150, help_text="Full name of the user")

    # Profile fields
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        blank=True, 
        null=True,
        help_text="Profile photo (optional)"
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?[1-9]\d{1,14}$')],
        blank=True,
        null=True,
        help_text="Contact phone number"
    )

    # Academic fields
    class_name = models.CharField(
        max_length=5, 
        choices=CLASS_CHOICES, 
        blank=True, 
        null=True,
        help_text="Class assigned (for students)"
    )
    student_id = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        unique=True,
        help_text="Unique student ID"
    )

    # Parent-Student relationship
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        limit_choices_to={'role': 'PARENT'},
        help_text="Parent of this student (if role is STUDENT)"
    )

    # Teacher fields
    subjects_taught = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Subjects taught by teacher (comma-separated)"
    )

    # Metadata
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Use email as username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'role']

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.full_name} ({self.role})"

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.first_name or self.full_name.split()[0]

    @property
    def is_student(self):
        return self.role == 'STUDENT'

    @property
    def is_teacher(self):
        return self.role == 'TEACHER'

    @property
    def is_parent(self):
        return self.role == 'PARENT'

    def can_view_student_data(self, student_user):
        """
        Check if current user can view data of given student
        """
        if self.is_teacher or self.is_superuser:
            return True
        if self.is_parent:
            return student_user in self.children.all()
        if self.is_student:
            return self == student_user
        return False


class UserProfile(models.Model):
    """
    Extended profile information for users
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')

    # Academic info
    admission_date = models.DateField(blank=True, null=True)
    graduation_date = models.DateField(blank=True, null=True)

    # Contact info
    address = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)

    # Academic performance
    overall_grade = models.CharField(max_length=2, blank=True, null=True)
    overall_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # Settings
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
    dark_mode = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return f"{self.user.full_name}'s Profile"
