from django.urls import path
from .views import VideoDetailsView, YoutubeAPIKey


urlpatterns = [
    path('details', VideoDetailsView.as_view(), name="video-details"),
    path('search', VideoDetailsView.as_view(), name="search-details"),
    path('create-key', YoutubeAPIKey.as_view(), name="video-details"),
]