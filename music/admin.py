# Almost every website in the world has admin section, a section that you can go and access database and delete users.
# So instead of creating that admin page, Django has already made it for you.

from django.contrib import admin
from .models import Album, Song

# We have to tell Django that Album class should have an admin interface.
# Register Album class as admin site.
# Then under music app, we can see Album.
admin.site.register(Album)
admin.site.register(Song)
