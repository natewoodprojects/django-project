from django.contrib import admin

# Register your models here.

from .models import Book, Plant
admin.site.register(Book)
admin.site.register(Plant)