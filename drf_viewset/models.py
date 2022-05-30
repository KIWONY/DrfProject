from django.db import models

# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=200, null=False)
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book