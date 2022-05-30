from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_viewset.views import BookViewSet

router = DefaultRouter()
router.register('book', BookViewSet , basename='book')


urlpatterns =[
    path('', include(router.urls))
]