📘 Bookshop Management System

📌 Project Description
<hr>
The Bookshop Management System is a simple Django web application that performs basic CRUD operations (Create, Read, Update, Delete) for managing books.

This project demonstrates how Django’s MVT architecture works in a real application.
<hr>
🚀 Features

View list of all books

Add a new book

Update book details

Delete a book

Simple UI using HTML and CSS
<hr>
🛠️ Technologies Used

Python 3.x

Django

SQLite (default database)

HTML

CSS
<hr>
📂 Project Structure
bookshop/
│
├── bookshop/        # Main project settings
├── books/           # Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── db.sqlite3
├── manage.py
└── README.md
<hr>
📊 Model Used
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.title
🔗 URL Patterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
]
⚙️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/bookshop.git
cd bookshop
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Django
pip install django
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Start Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
<hr>
🎯 Learning Outcomes

Understanding Django MVT architecture

Working with Models and ORM

Handling forms and templates

Performing CRUD operations

Connecting project to GitHub
