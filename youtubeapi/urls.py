from django.urls import path
from .views import VideoDetailsView, YoutubeAPIKey,SearchVideo


urlpatterns = [
    path('details', VideoDetailsView.as_view(), name="video-details"),
    path('search', SearchVideo.as_view(), name="search-details"),
    path('create-key', YoutubeAPIKey.as_view(), name="video-details"),
]