
# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from drfbackend.models import Article, Music
from drfbackend.serializers import ArticleSerializer, MusicSerializer

# ------------Article------------
@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer =ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request, slug):
    try:
        article = Article.objects.get(slug=slug)

    except Article.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# ----------Music----------
class MusicList(APIView):
    def get(self, request, format=None):
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicDetail(APIView):
    def get_object(self, slug):
        try:
            return Music.objects.get(slug=slug)
        except Music.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        music = self.get_object(slug)
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = MusicSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        snippet = self.get_object(slug)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)