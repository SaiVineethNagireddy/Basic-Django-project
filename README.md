📘 Bookshop Management System (Django CRUD)
📌 Project Overview

The Bookshop Management System is a basic Django web application that performs CRUD operations (Create, Read, Update, Delete) on books.

This project demonstrates:

Django MVT architecture

Models and ORM

URL routing

Templates

Static files

CRUD operations

🚀 Features

📖 View all books

➕ Add a new book

✏️ Update book details

❌ Delete a book

🎨 Basic styling using static CSS

🛠️ Technologies Used

Python 3.x

Django

SQLite (default database)

HTML

CSS

📂 Project Structure
bookshop/
│
├── bookshop/          # Main project folder
├── books/             # Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── db.sqlite3
├── manage.py
└── README.md
🗂️ MVT Architecture Used

Model → Defines Book table in database

View → Handles business logic

Template → HTML files for UI

URL → Routes requests to views

📊 Book Model Example
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.title
🔗 URL Patterns
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
]
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/bookshop.git
cd bookshop
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install django
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Run Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
