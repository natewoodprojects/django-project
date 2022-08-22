from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Book, Plant, Plants

from .forms import PlantForm



def index(request):
    return render(request, 'plants.html')

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

def plants_homepage(request):
    plant = Plant.objects.get(pk=1)
    plants = Plant.objects.all()
    full_plant = Plants.objects.all()
    
    return render(request, 'plants.html', {"full_plant": full_plant,'plant':plant, 'plants':plants})

def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            light = form.cleaned_data['light']
            water = form.cleaned_data['water']
            humidity = form.cleaned_data['humidity']
            soil = form.cleaned_data['soil']
            fertilizer = form.cleaned_data['fertilizer']
            toxcicity = form.cleaned_data['toxcicity']
            notes = form.cleaned_data['notes']           
            p = Plants(user_id=1, name=name,type=type,light=light, water=water, humidity=humidity, soil=soil, fertilizer=fertilizer,  toxcicity=toxcicity, notes=notes )
            p.save()
            return HttpResponseRedirect("/plants")
    form = PlantForm(request.POST)
    return render(request, "new_plant.html", {'form': form})