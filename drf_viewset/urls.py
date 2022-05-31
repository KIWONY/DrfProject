from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_viewset.views import BookViewSet, LogViewSet

router = DefaultRouter()
router.register('book', BookViewSet , basename='book')
router.register('log', LogViewSet, basename='log')

urlpatterns =[
    path('', include(router.urls)),
]