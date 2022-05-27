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