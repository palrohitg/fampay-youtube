from django.urls import path
from .views import VideoDetailsView, YoutubeAPIKey


urlpatterns = [
    path('details', VideoDetailsView.as_view(), name="video-details"),
    path('create-key', YoutubeAPIKey.as_view(), name="video-details"),
]