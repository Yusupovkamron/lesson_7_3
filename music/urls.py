from django.urls import path, include
from .views import LandingPageAPIView, ArtistApiView, SongsApiView, SongDetailAPIView, AlbomAPIViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("alboms", viewset=AlbomAPIViewSet)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path("", include(router.urls)),
    path('artists/', ArtistApiView.as_view(), name="artists"),
    path('songs/', SongsApiView.as_view(), name="songs"),
    path('songs/<int:id>/', SongDetailAPIView.as_view(), name="song-detail"),
]