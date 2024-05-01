from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer
import json

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


class AlbomtApiView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serialisers = AlbomSerializer(alboms, many=True)
        return Response(data=serialisers.data)



class SongsApiView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serialisers = SongsSerializer(songs, many=True)
        data = serialisers.data
        # with open("../data.json", 'w') as f:
        #     json.dump(data, f, indext=6)
        return Response(data=serialisers.data)

