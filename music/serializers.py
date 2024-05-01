from rest_framework import serializers
from .models import Artist, Albom, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meda:
        mode = Artist
        fields = "__all__"


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()


    class Meda:
        mode = Albom
        fields = "__all__"


class SongsSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer()




    class Meda:
        mode = Songs
        fields = "__all__"



