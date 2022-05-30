from django.shortcuts import render


from rest_framework import viewsets, mixins

from drf_viewset.models import Book
from drf_viewset.serializers import BookSerializer

#--------------Generic View Set-------------------------
class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer