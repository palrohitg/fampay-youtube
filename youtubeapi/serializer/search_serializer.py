from rest_framework import serializers
from youtubeapi.models import VideoDetail


class SearchSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = VideoDetail
        fields = '__all__'

    def to_internal_value(self, data):
        return {
            'title': data.get('title'),
            'description': data.get('description'),
        }

    def validate(self, data):
        title = data.get('title')
        description = data.get('description')

        if not title and not description:
            raise serializers.ValidationError("Either title or description is required in the query parameters.")

        return data

