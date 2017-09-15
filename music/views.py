# Views are simply python functions that take user request and give a response in some kind of way.
# Most of the time, the user is just going to request a webpage and just give a webpage.
# Each URL in urls.py is connected to a view, i.e. each URL is connected to an HTML response.

from django.http import HttpResponse

# request is an HTML request
def index(request):
    return HttpResponse("<h1> This is the Music app homepage </h1>")

# album_id came from music/urls.py
# So whenever this function is called, it returns this HTTP response.
def detail(request, album_id):
    return HttpResponse("<h2> Details for Album ID:" + str(album_id) + "</h2>")