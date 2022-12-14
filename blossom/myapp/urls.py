from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
    path('plants', views.plants_homepage, name='plants_homepage'),
    path('create', views.create_plant, name='creation_page')
]