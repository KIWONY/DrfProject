from django.db import models

# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=200, null=False)
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book




class Log(models.Model):
    log = models.TextField(max_length=500,null=False)
    writer = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.log