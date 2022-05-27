from django.urls import path

from drfbackend.views import article_list, article_detail

urlpatterns = [
    path('articles/',article_list),
    path('articles/<slug:slug>/', article_detail),
]