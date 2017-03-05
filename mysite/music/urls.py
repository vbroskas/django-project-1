from django.conf.urls import url
from . import views

#ALWAYS NAMESPACE YOUR URL PATTERNS TO ASSOCIATE A URL WITH ITS SPECIFIC APP
app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/21
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]
