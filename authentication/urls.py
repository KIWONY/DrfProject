from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.views import JournalViewSet

router = DefaultRouter()
router.register('journal', JournalViewSet , basename='journal')


urlpatterns =[
    path('', include(router.urls)),
]