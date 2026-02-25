from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST": #if we want to submit the data
        form = RegisterForm(request.POST) #take the submitted data and bind it for validation
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user) # this creates a session in the form of a cookie
            return redirect('book_list')
    return render(request, 'login.html')

def user_logout(request):
    logout(request) # this deletes the session from the database
    return redirect('login')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid(): #it checks if everything is filled properly
        book = form.save(commit=False) #Here rather than saving to the db we just created object due to added_by
        book.added_by = request.user
        book.save()
        return redirect('book_list')
    return render(request, 'add_book.html', {'form': form})

@login_required
def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book) #instance = book. which means "This form is for editing THIS specific book"
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'add_book.html', {'form': form})

@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')

@login_required
def sell_book(request, id):
    book = get_object_or_404(Book, id=id)
    if book.stock > 0:
        book.stock -= 1
        book.save()
    return redirect('book_list')