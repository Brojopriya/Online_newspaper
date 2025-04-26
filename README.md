📰 Online Newspaper (Django Project)
An online news portal built using Django, featuring:

📰 Article browsing

🔎 Search functionality

🗂️ Category filtering

📬 Newsletter subscription




🚀 Quick Start Guide
# 1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/online-newspaper.git
cd online-newspaper
# 2. Create & Activate Virtual Environment
bash
# Create virtual environment

python -m venv venv

# Activate it
# For Mac/Linux
source venv/bin/activate
# For Windows
venv\Scripts\activate
# 3. Install Required Packages
bash


pip install -r requirements.txt
# 4. Apply Database Migrations
bash
Copy code
python manage.py migrate
# 5. Create Admin Superuser (Optional)
bash
Copy code
python manage.py createsuperuser
# 6. Start the Development Server
bash
Copy code
python manage.py runserver
# 7. Open the App
Visit 👉 http://127.0.0.1:8000/

🛠 Features
Full article browsing with details page

Powerful search across titles and content

Filter articles by category

Static "About Us" and "Contact" pages

User-friendly mobile-first responsive design

Easy backend management via Django Admin Panel

Newsletter signup functionality (basic version)

📋 Requirements
Python 3.8+

Django 5.x

(Install using requirements.txt)

