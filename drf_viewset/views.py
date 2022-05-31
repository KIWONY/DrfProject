from django.shortcuts import render


from rest_framework import viewsets, mixins

from drf_viewset.models import Book, Log
from drf_viewset.serializers import BookSerializer, LogSerializer


#--------------Generic View Set-------------------------
class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



#----------------Model View Set----------------------

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
#   lookup_field is pk(default)

