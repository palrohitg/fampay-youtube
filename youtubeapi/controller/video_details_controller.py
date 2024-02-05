from youtubeapi.dbmanager.youtube import VideoDetailsDBManager


class VideoDetailController:

    def __init__(self):
        pass
    def create_video_details(self, video_detail):
        VideoDetailsDBManager().create_video_details(video_detail)

    def get_video_details_desc(self, limit):
        return VideoDetailsDBManager().get_video_details(limit)