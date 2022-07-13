from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'artist'

class Album(models.Model):
    name = models.CharField(max_length=100)
    released_in = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2022)])

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'album'

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'song'

