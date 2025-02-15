# Academic ChatBot Backend

## 📌 Project Overview
The **Academic ChatBot** is a smart assistant designed to help students navigate their academic journey. It provides guidance on courses, academic progress, timetables, career advice, and mental health resources.

This repository contains the **Django backend**, which provides API endpoints for student authentication, academic tracking, course management, and chatbot interactions.

## 🚀 Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **API Documentation**: Swagger / Postman Collection

## 📂 Project Structure
```
academic_chatbot_backend/
│-- academic_chatbot/         # Main project folder
│   │-- settings.py           # Django settings
│   │-- urls.py               # API routes
│-- students/                 # App for student management
│   │-- models.py             # Database models
│   │-- views.py              # API views
│   │-- serializers.py        # Data serialization
│-- courses/                  # App for course management
│-- timetable/                # App for timetable handling
│-- chatbot/                  # App for chatbot logic
│-- requirements.txt          # Project dependencies
│-- manage.py                 # Django CLI
```

## ⚡ Getting Started
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/academic_chatbot_backend.git
cd academic_chatbot_backend
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/academic_chatbot_db
```

### 5️⃣ Apply Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```

## 🔥 API Endpoints
| Method | Endpoint                  | Description |
|--------|---------------------------|-------------|
| POST   | `/api/auth/register/`     | Register a new student |
| POST   | `/api/auth/login/`        | Login and get JWT token |
| GET    | `/api/courses/`           | Get all courses |
| GET    | `/api/students/{id}/progress/` | Get student academic progress |
| POST   | `/api/students/{id}/enroll/`   | Enroll student in a course |
| GET    | `/api/timetable/{id}/`    | Get student timetable |

## 🛠️ Development & Contribution
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit changes and push
4. Create a pull request (PR)

## 📜 License
This project is licensed under the **MIT License**.

## 📞 Contact
For questions or collaboration, reach out to **[your email or GitHub link]**.
