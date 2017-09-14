# Views are simply python functions that take user request and give a response in some kind of way.
# Most of the time, the user is just going to request a webpage and just give a webpage.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the Music app homepage </h1>")