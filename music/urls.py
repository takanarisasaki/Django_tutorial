from django.conf.urls import url
from . import views

urlpatterns = [
    # If user request a homepage for /music
    # index is a homepage for section
    # Whenever this URL is requested, we go to views.py and call the function index.
    url(r'^$', views.index, name='index')
]