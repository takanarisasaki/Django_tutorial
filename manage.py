#!/usr/bin/env python
import os
import sys

# This file allows to access database, create users for website, etc.
# DO NOT TOUCH OR EDIT THIS FILE.
# To run server: "python manage.py runserver"
# To create app: "python manage.py startapp <app_name>"

# To run Django database API, run "python manage.py shell".
# >>> from music.models import Album, Song
# >>> Album.objects.all()
# >>> a = Album(artist="Taylor Swift", album_title="Red", genre="Country", album_logo="https://upload.wikimedia.org/wikipedia/en/e/e8/Taylor_Swift_-_Red.png")
# >>> a.save()      # This command saves "a" object to database.
# >>> b = Album()
# >>> b.artist = "Myth"
# >>> b.album_title = "High School"
# >>> b.genre = "Punk"
# >>> b.album_logo = "http://paigeentwistle.com/wp-content/uploads/2015/12/myth.jpg"
# >>> a.save()
# >>> Album.objects.filter(id=1)
# >>> Album.objects.filter(artist__startswith="Taylor")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
