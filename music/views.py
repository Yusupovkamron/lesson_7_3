from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer,  SongsSerializer,AlbomSerializer
import json
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hi laze developers"})

    def post(self, request):
        return Response(data={"post api": "this is post api"})


class ArtistApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serialisers = ArtistSerializer(artists, many=True)
        return Response(data=serialisers.data)


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer





class SongSetAPIView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['^title']
    pagination_class = LimitOffsetPagination




    # def get(self, request, id):
    #     try:
    #         song = Songs.objects.get(id=id)
    #         serializer = SongsSerializer(song)
    #         return Response(data=serializer.data)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    # def patch(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(instance=song, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # def put(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(instance=song, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     song.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


