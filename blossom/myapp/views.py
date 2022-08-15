from django.shortcuts import render

from django.http import HttpResponse

from .models import Book



def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/book/1">This should be a book</a>')

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

def plants_homepage(request):
    return render(request, 'plants.html')