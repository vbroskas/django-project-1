
from django.shortcuts import render, get_object_or_404 #lets us use templates
from .models import Album, Song


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

    context = {'all_albums': all_albums }

    return render(request, 'music/index.html', context)



def detail(request, album_id): # request is just the HTML request
    #first query database to see if there is an album with the id requested

    #instead of using a try/except with:   album = Album.objects.get(id = album_id)
    #we instead use:
    album = get_object_or_404(Album, id=album_id)
    context = {'album': album}

    return render(request, 'music/detail.html', context)



def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    context = {'album': album}

    try:
        selected_song = album.song_set.get(id = request.POST['song'])

    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {{
        'album' : album,
        'error_messsage' : "You did not select a valid song!"

        }}) #sending them back to the details page to get that error notification

    else:
        #if all goes well, we need to update the database, and set the is_favorite attribute to true!
        if selected_song.is_favorite == True:
            selected_song.is_favorite = False
        else:
            selected_song.is_favorite = True
        selected_song.save() # !!! make sure to save your changes!!
        return render(request, 'music/detail.html', context)
