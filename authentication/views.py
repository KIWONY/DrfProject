from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.models import Journal
from authentication.serializers import JournalSerializer
from permissions import IsAuthor


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [IsAuthenticated,IsAuthor]

