#!/usr/bin/env python
"""
Sample Data Creation Script for Student Progress Tracker
Run this script to populate the database with demo data
"""

import os
import sys
import django
from datetime import datetime, date

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracker.settings')
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_sample_users():
    """Create sample users for testing"""
    print("Creating sample users...")

    # Create admin
    admin, created = User.objects.get_or_create(
        email='admin@school.com',
        defaults={
            'username': 'admin@school.com',
            'full_name': 'System Administrator',
            'role': 'ADMIN',
            'is_staff': True,
            'is_superuser': True,
        }
    )
    if created:
        admin.set_password('admin123')
        admin.save()
        print(f"✅ Created admin: {admin.email}")

    # Create teacher
    teacher, created = User.objects.get_or_create(
        email='sarah.johnson@school.com',
        defaults={
            'username': 'sarah.johnson@school.com',
            'full_name': 'Dr. Sarah Johnson',
            'role': 'TEACHER',
            'subjects_taught': 'Mathematics, Physics',
        }
    )
    if created:
        teacher.set_password('teacher123')
        teacher.save()
        print(f"✅ Created teacher: {teacher.full_name}")

    # Create student
    student, created = User.objects.get_or_create(
        email='john.smith@school.com',
        defaults={
            'username': 'john.smith@school.com',
            'full_name': 'John Smith',
            'role': 'STUDENT',
            'class_name': '10A',
            'student_id': 'STU001',
        }
    )
    if created:
        student.set_password('student123')
        student.save()
        print(f"✅ Created student: {student.full_name}")

    # Create parent
    parent, created = User.objects.get_or_create(
        email='robert.smith@parent.com',
        defaults={
            'username': 'robert.smith@parent.com',
            'full_name': 'Robert Smith',
            'role': 'PARENT',
        }
    )
    if created:
        parent.set_password('parent123')
        parent.save()
        print(f"✅ Created parent: {parent.full_name}")

        # Link parent to child
        student.parent = parent
        student.save()
        print(f"   Linked to child: {student.full_name}")

def main():
    """Main function to create sample data"""
    print("🚀 Creating sample data for Student Progress Tracker\n")

    try:
        create_sample_users()

        print("\n🎉 Sample data creation completed!")
        print("\n📝 You can now login with these accounts:")
        print("   Admin: admin@school.com / admin123")
        print("   Teacher: sarah.johnson@school.com / teacher123")
        print("   Student: john.smith@school.com / student123")
        print("   Parent: robert.smith@parent.com / parent123")
        print("\n🌐 Access the application at: http://127.0.0.1:8000/")

    except Exception as e:
        print(f"❌ Error creating sample data: {str(e)}")

if __name__ == '__main__':
    main()
