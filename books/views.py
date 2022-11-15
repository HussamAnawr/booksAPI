from django.shortcuts import render
from .models import Book
from django.views.generic import ListView

# Create your views here.
class BookList(ListView):
    model = Book
    template_name = 'books.html'