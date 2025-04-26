Online Newspaper (Django Project)
An online news portal built using Django, featuring article browsing, search, category filtering, newsletter subscriptions, and a responsive layout inspired by The Daily Star.

📂 Project Structure

newspaper_project/
├── news/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── home.html
│   │   ├── article_detail.html
│   │   ├── search_result.html
│   │   ├── category.html
│   │   ├── about.html
│   │   └── contact.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── newspaper_project/
│   └── settings.py
│   └── urls.py
└── manage.py

🛠️ Setup Instructions

1. Clone the repository
git clone https://github.com/yourusername/online-newspaper.git
cd online-newspaper

2.Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3.Install dependencies
pip install -r requirements.txt

4.Apply migrations and create superuser
python manage.py migrate
python manage.py createsuperuser

5.Run the development server
python manage.py runserver

6.Access the app
Visit: http://127.0.0.1:8000/
