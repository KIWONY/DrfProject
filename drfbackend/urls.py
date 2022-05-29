from django.urls import path

from drfbackend.views import article_list, article_detail, MusicList, MusicDetail

urlpatterns = [
    path('articles/',article_list),
    path('articles/<slug:slug>/', article_detail),
    path('music/',MusicList.as_view()),
    path('music/<slug:slug>',MusicDetail.as_view())
]