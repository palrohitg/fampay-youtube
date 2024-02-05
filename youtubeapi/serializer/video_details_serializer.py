from rest_framework import serializers
from youtubeapi.models import VideoDetail


class VideoDetailSerializer(serializers.ModelSerializer):
    limit = serializers.IntegerField(min_value=1, required=False, default=10)

    class Meta:
        model = VideoDetail
        fields = '__all__'

    def validate_limit(self, value):
        try:
            value = int(value)
            if value < 1:
                raise serializers.ValidationError("Limit should be a positive integer.")
        except ValueError:
            raise serializers.ValidationError("Limit should be a valid integer.")
        return value

    def to_internal_value(self, data):
        return {'limit': data.get('limit', 10)}

