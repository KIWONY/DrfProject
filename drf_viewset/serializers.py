from rest_framework import serializers

from drf_viewset.models import Book, Log


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'



class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = '__all__'