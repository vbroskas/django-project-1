from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404 #so we can use 404 response
from .models import Album
from django.shortcuts import render #lets us use templates

# Create your views here.

'''
#WOULDNT NORMALLY DO IT LIKE THIS, WOULD USE A TEMPLATE INSTEAD. SHOULDNT HAVE html MIXED IN WITH PYTHON
def index(request):
    #need to connect to database and get all the albums
    #all_albums will store the result of our database call
    all_albums = Album.objects.all()
    #now loop through each of the all_albums
    html = ''
    for album in all_albums:
        #build a link for each album
        url = '/music/' + str(album.id) + '/'

        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    return HttpResponse(html)
'''
#USING A TEMPLATE
def index(request):
    all_albums = Album.objects.all()

    context = {
        'all_albums': all_albums

    }
    return render(request, 'music/index.html', context)

def detail(request, album_id): # request is just the HTML request
    return HttpResponse('<h2>details for album_id:' + str(album_id) + '</h2>')
