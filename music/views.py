from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer,  SongsSerializer,AlbomSerializer
import json
from rest_framework import status
from rest_framework.viewsets import ModelViewSet



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



class SongsApiView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serialisers = SongsSerializer(songs, many=True)
        data = serialisers.data
        # with open("../data.json", 'w') as f:
        #     json.dump(data, f, indext=6)
        return Response(data=serialisers.data)


class SongDetailAPIView(APIView):
    def get(self, request, id):
        try:
            song = Songs.objects.get(id=id)
            serializer = SongsSerializer(song)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongsSerializer(instance=song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongsSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = Songs.objects.get(id=id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


