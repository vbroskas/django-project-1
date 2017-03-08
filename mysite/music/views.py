# Using generic views

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView #whenever you want to make a form that will create a new object, you need this. UpdateView is for editing an object, DeleteView for deleting an object
from .models import Album


# for making generic views, instead of using functions, we will be using classes
# there are generic views you can inherit, list, detail, etc


# Whenever you use a ListView, it will query the database and return it in an object called object_list
class IndexView(generic.ListView):
    # First specify which template we are using-
    template_name = 'music/index.html'

    # to override the name of object_lsit:
    context_object_name = 'all_albums'
    # then make query set function
    # Query database for whatever we need, which in this case is all albums
    def get_queryset(self):
        return Album.objects.all()


# Whenever you are using a detail view, it expects a primary key! so add it in the urls.py
class DetailView(generic.DetailView):

    # First say which model you are trying to get the details of
    model = Album

    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    #1) you are trying to create a new object, what kind of object is it?
    model = Album
    #2 what fields do you need in the form? ie what attributes do you want me to allow the user to fill out?
    fields = ['artist', 'album_title', 'genre', 'album_logo']
