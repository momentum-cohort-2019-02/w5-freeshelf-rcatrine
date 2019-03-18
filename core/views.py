from django.shortcuts import render
from core.models import Book, Author, Category, awk, bash, html, javascript, ruby
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    """View function for home page of site."""


    num_books = Book.objects.all().count()  
    num_authors = Author.objects.count()
    num_categories = Category.objects.count()
    
   
    
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_categories': num_categories,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category

class awkListView(generic.ListView):
    model = awk

class awkDetailView(generic.DetailView):
    model = awk

class bashListView(generic.ListView):
    model = bash

class bashDetailView(generic.DetailView):
    model = bash

class htmlListView(generic.ListView):
    model = html

class htmlDetailView(generic.DetailView):
    model = html

class javascriptListView(generic.ListView):
    model = javascript

class javascriptDetailView(generic.DetailView):
    model = javascript

class rubyListView(generic.ListView):
    model = ruby

class rubyDetailView(generic.DetailView):
    model = ruby




