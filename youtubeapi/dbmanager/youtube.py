from youtubeapi.models import VideoDetail,YoutubeAPIKey


class VideoDetailsDBManager:

    def create_video_details(self, video_details_data):
        try:
            VideoDetail.objects.bulk_create(video_details_data)
        except Exception as e:
            print(e)

    def get_video_details(self, limit=10):
        try:
            limit = int(limit)
            return VideoDetail.objects.order_by('-published_at')[:limit]
        except Exception as e:
            print(e)
        return None

    def get_youtube_api_key(self):
        try:
            return YoutubeAPIKey.objects.filter(is_active=True).first()
        except Exception as e:
            print(e)
        return None


    def create_youtube_api_key(self, key):
        try:
            return YoutubeAPIKey.objects.create(key=key, is_active=True)
        except Exception as e:
            print(e)
        return None

    def get_video_all_details(self):
        try:
            return VideoDetail.objects.filter()
        except Exception as e:
            print(e)
        return None

    def get_video_all_details_filter(self, filter):
        try:
            return VideoDetail.objects.filter(**filter)
        except Exception as e:
            print(e)
        return None



