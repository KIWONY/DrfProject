from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, null= False)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Article(models.Model):
    subtitle = models.CharField(max_length=200, null=False)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subtitle



class Music(models.Model):
    song = models.CharField(max_length=200, null=False)
    artist = models.TextField()
    released_in = models.IntegerField(validators=[MinValueValidator(1950),MaxValueValidator(2022)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song