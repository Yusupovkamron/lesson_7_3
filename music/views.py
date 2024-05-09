from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs, Country
from .serializers import ArtistSerializer,  SongsSerializer,AlbomSerializer, CountrySerializer
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


class CountrySetApiView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^title']
    pagination_class = LimitOffsetPagination
