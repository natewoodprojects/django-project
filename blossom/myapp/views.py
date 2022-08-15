from django.shortcuts import render

from django.http import HttpResponse

from .models import Book



def index(request):
    return render(request, 'plants.html')

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

def plants_homepage(request):
    return render(request, 'plants.html')

def create_plant(request):
    return render(request, 'new_plant.html')