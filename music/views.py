# Views are simply python functions that take user request and give a response in some kind of way.
# Most of the time, the user is just going to request a webpage and just give a webpage.
# Each URL in urls.py is connected to a view, i.e. each URL is connected to an HTML response.
# Whenever we have a view, we need to return something.

from django.http import HttpResponse
# Since we are going to work with Album information, we need to import it.
from .models import Album
# from django.template import loader
from django.shortcuts import render

# When we don't have a webpage to show, we want to send back 404 HTTP error.
from django.http import Http404


# # request is an HTML request
# def index(request):
#     # First, we need to connect to the database and get all of the Albums.
#     # all_albums will store the results of the database call.
#     # Album.objects.all() will connect to the database, look inside Album table, and store it inside all_albums
#     all_albums = Album.objects.all()
#     html = ''
#
#     # Now that we have a list of albums, we need to loop through them so that we can access them one by one.
#     for album in all_albums:
#         # For each album, we want to make a link.
#         # Cannot concatenate integer with string, so need to convert to string first.
#         url = '/music/' + str(album.id) + '/'
#         html += '<a href=" ' + url + ' ">' + album.album_title + '</a> <br>'
#
#     return HttpResponse(html)


# # Using template to separate our front-end code from back-end code
# # First, make a template file in /music/templates/music/index.html
# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#
#     # Whenever we pass all_albums information to our template (music/index.html),
#     # we pass it through a dictionary. We often name that dictionary "context".
#     context = {
#         'all_albums': all_albums,
#     }
#
#     return HttpResponse(template.render(context, request))


# Using "render" rather than HttpResponse to send back a response.
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


# # album_id came from music/urls.py
# # So whenever this function is called, it returns this HTTP response.
# def detail(request, album_id):
#     return HttpResponse("<h2> Details for Album ID:" + str(album_id) + "</h2>")

# Check if the album exist. If not, raise Http404 Error.
def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    return render(request, 'music/details.html', {'album': album})