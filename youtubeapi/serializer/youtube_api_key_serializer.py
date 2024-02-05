from rest_framework import serializers
from youtubeapi.models import YoutubeAPIKey


class YoutubeAPIKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = YoutubeAPIKey
        fields = ["key"]
