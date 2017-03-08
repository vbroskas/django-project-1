from django.conf.urls import url
from . import views

#ALWAYS NAMESPACE YOUR URL PATTERNS TO ASSOCIATE A URL WITH ITS SPECIFIC APP
app_name = 'music'

# each URL pattern must be hooked up to a view function
# since we have classes in views.py, we have to reference the class then convert it to a view
urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/21
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #need to assign a URL to the AlbumCreate viwe
    #matches /music/album/add/    doesnt need a PK because it is just being made, it doesnt have one yet
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

]
