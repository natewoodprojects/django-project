from django.shortcuts import render

from django.http import HttpResponse

from .models import Book, Plant



def index(request):
    return render(request, 'plants.html')

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

def plants_homepage(request):
    plant = Plant.objects.get(pk=1)
    plants = Plant.objects.all()
    return render(request, 'plants.html', {'plant':plant, 'plants':plants})

def create_plant(request):

    # p = Plant(name=, type=, water_ammount=, description=)

    # name = models.CharField(max_length=200)
    # type = models.CharField(max_length=200)
    # water_ammount = models.DecimalField(decimal_places=0, max_digits=10)
    # description = models.CharField(max_length=500)

    # b = Book(title=, pub_date=)


    return render(request, 'new_plant.html')