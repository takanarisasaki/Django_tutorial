from django.conf.urls import url
from . import views

urlpatterns = [
    # If user request a homepage for /music
    # index is a homepage for section
    # Whenever this URL is requested, we go to views.py and call the function index.
    # Regular expression: '^' means beginning, and '$' means ending.
    url(r'^$', views.index, name='index'),   # /music/

    # views is the name of the module, and detail is the name of the function defined in views.py.
    # If you have name, it allows you to do stuffs in HTML.
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')# /music/71/
]
