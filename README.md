# 🎓 Student Progress Tracker

A comprehensive full-stack web application for tracking student academic progress, built with Django, Django REST Framework, PostgreSQL, HTML, CSS, JavaScript, and Chart.js.

![Student Progress Tracker](https://img.shields.io/badge/Django-4.2.7-green)
![DRF](https://img.shields.io/badge/DRF-3.14.0-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)
![Chart.js](https://img.shields.io/badge/Chart.js-Latest-orange)

## ✨ Features

### 🔐 Role-Based Authentication
- **Student, Teacher, Parent, Admin** roles
- Custom user model with profiles
- Parent-child account linking
- Session management

### 📊 Dashboard & Analytics
- Role-specific dashboards
- Interactive Chart.js visualizations
- Performance metrics and statistics
- Real-time progress tracking

### 📚 Academic Management
- Subject and class management
- Marks entry and grade calculation
- Performance analytics
- Progress reports

### ✅ Task Management
- Assignment creation and tracking
- Due date management
- File uploads and submissions
- Progress monitoring

### 📅 Attendance System
- Daily attendance marking
- Attendance statistics
- Alert system for low attendance
- Detailed attendance reports

### 🎯 Goals & Gamification
- Goal setting and tracking
- Achievement badges
- Leaderboards
- Progress rewards

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7 + Django REST Framework
- **Database**: PostgreSQL (SQLite for development)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5.3.0
- **Charts**: Chart.js
- **Icons**: Font Awesome 6.4.0

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- PostgreSQL (optional - can use SQLite for development)
- Git

### 1. Clone or Extract Project
```bash
# Extract the zip file and navigate to project directory
cd student-progress-tracker
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
# Copy and edit .env file with your settings
# For development, you can use the default SQLite database
```

### 5. Setup Database
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Sample Data (Optional)
```bash
# Go back to project root
cd ..
python create_sample_data.py
```

### 7. Create Superuser
```bash
cd backend
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

### 9. Access Application
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 👥 Demo Accounts

After running the sample data script:

- **Admin**: admin@school.com / admin123
- **Teacher**: sarah.johnson@school.com / teacher123
- **Student**: john.smith@school.com / student123
- **Parent**: robert.smith@parent.com / parent123

## 📁 Project Structure

```
student-progress-tracker/
├── backend/
│   ├── manage.py                   # Django management script
│   ├── tracker/                    # Django project settings
│   │   ├── settings.py            # Main settings
│   │   ├── urls.py                # URL configuration
│   │   ├── wsgi.py                # WSGI config
│   │   └── asgi.py                # ASGI config
│   └── apps/                      # Django applications
│       ├── users/                 # User management
│       ├── subjects/              # Academic subjects
│       ├── tasks/                 # Task management
│       ├── attendance/            # Attendance tracking
│       ├── goals/                 # Goals and habits
│       └── resources/             # Resource management
├── templates/                     # HTML templates
│   ├── base.html                  # Base template
│   ├── login.html                 # Login page
│   ├── dashboard.html             # Main dashboard
│   └── signup.html                # Registration page
├── static/                        # Static files
│   ├── css/style.css              # Main stylesheet
│   └── js/main.js                 # JavaScript functionality
├── media/                         # User uploads
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
├── create_sample_data.py          # Sample data script
└── README.md                      # This file
```

## 🎨 Features by Role

### 👨‍🎓 For Students:
- View grades and academic progress
- Track assignments and deadlines
- Monitor attendance records
- Set and track personal goals
- Access study resources
- View achievement badges

### 👨‍🏫 For Teachers:
- Manage student records
- Enter marks and grades
- Create and assign tasks
- Mark daily attendance
- Upload educational resources
- Generate progress reports

### 👨‍👩‍👧‍👦 For Parents:
- Monitor child's academic progress
- View attendance records
- Track assignment completion
- Communicate with teachers
- Access progress reports

### 👨‍💼 For Administrators:
- Manage all users and roles
- Configure academic settings
- Generate system reports
- Monitor system usage
- Manage data and backups

## 🔧 Configuration

### Database Configuration
```python
# For PostgreSQL (production)
DATABASE_URL=postgresql://username:password@localhost:5432/student_tracker

# For SQLite (development)
DATABASE_URL=sqlite:///./db.sqlite3
```

### Environment Variables
Update `.env` file with your configuration:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `DATABASE_URL`: Database connection string

## 📊 API Endpoints

The application provides a comprehensive REST API:

- `/api/users/` - User management
- `/api/subjects/` - Subject management
- `/api/tasks/` - Task operations
- `/api/attendance/` - Attendance records
- `/api/goals/` - Goals and habits
- `/api/resources/` - Resource management

## 🎨 UI Features

- **Responsive Design**: Works on all devices
- **Dark Mode**: Theme toggle support
- **Interactive Charts**: Chart.js visualizations
- **Modern UI**: Bootstrap 5 components
- **Real-time Updates**: Dynamic content loading

## 🚀 Deployment

### Development
```bash
python manage.py runserver
```

### Production
1. Set `DEBUG=False` in `.env`
2. Configure proper database
3. Set up web server (nginx/apache)
4. Use WSGI server (gunicorn/uwsgi)
5. Configure static file serving

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support:
- Check the documentation
- Review the code comments
- Create GitHub issues
- Contact the development team

---

**Built with ❤️ for educational excellence**
