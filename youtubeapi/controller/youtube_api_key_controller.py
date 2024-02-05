from youtubeapi.dbmanager.youtube import VideoDetailsDBManager


class YoutubeAPIKeyController:

    def create_api_key(self, data):
        key = data.get('key')
        return VideoDetailsDBManager().create_youtube_api_key(key=key)