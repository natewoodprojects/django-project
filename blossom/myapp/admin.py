from django.contrib import admin

# Register your models here.

from .models import Book, Plant, Plants
admin.site.register(Book)
admin.site.register(Plant)
admin.site.register(Plants)