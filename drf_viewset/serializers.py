from rest_framework import serializers

from drf_viewset.models import Book


class BookSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'