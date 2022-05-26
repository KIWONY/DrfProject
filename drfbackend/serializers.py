from rest_framework import serializers

from drfbackend import models
from drfbackend.models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField(max_length=200)
    date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.date = validated_data.get("date", instance.date)
        instance.save()
        return instance