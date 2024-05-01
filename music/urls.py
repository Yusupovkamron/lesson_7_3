from django.urls import path
from .views import LandingPageAPIView, ArtistApiView, AlbomtApiView, SongsApiView

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path('artists/', ArtistApiView.as_view(), name="artists"),
    path('alboms/', AlbomtApiView.as_view(), name="alboms"),
    path('songs/', SongsApiView.as_view(), name="songs"),
]