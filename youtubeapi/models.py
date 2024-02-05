from django.db import models


# Create your models here.
class VideoDetail(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    thumbnail_url = models.CharField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-published_at']),
        ]
        db_table = 'VideoDetail'


class YoutubeAPIKey(models.Model):
    key = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['key']),
        ]
        db_table = 'YoutubeAPIKey'