# A model is a blueprint for your database.
# It is basically how you are going to store data in database.
# Each variable in the class will become a column in the table.

from django.db import models

# Whenever we run the server, we look into INSTALLED_APPS in settings.py and check
# if all the apps installed, it is going to look at the models and check if
# those models match the database. So every time we add something to the model,
# we need to make that change reflect to the database.
# To do that, run "python manage.py makemigrations music". (This command only makes the change file with SQP commands).
# We made changes to the music model
# To check the SQL command, run "python manage.py sqlmigrate music 0001".
# So migration is simply making change to the database (ex. by creating tables,
# creating new columns in table that already existed, etc.
# Finally, we run "python manage.py migrate" to run the change file created by makemigrations.

# Album table has 4 columns.
# Django actually creates another column, which is unique ID number.
# First album we create will be an ID of 1, then 2, etc.

# | ID | artist | album_title | genre | album_logo |
#  ________________________________________________

# Migrations are needed only when we make a new table or when we make a new column of a table.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    # You can specify what you want to print out when running "Album.objects.all()".
    def __str__(self):
        return self.album_title + " - " + self.artist


# Each song WILL be linked to an album.
# If we delete an album, we want to delete all songs associated to that album, so
# "on_delete=models.CASCADE" will do that.
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title