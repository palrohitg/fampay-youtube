from youtubeapi.dbmanager.youtube import VideoDetailsDBManager


class VideoDetailController:

    def __init__(self):
        pass
    def create_video_details(self, video_detail):
        VideoDetailsDBManager().create_video_details(video_detail)

    def get_video_details_desc(self, limit):
        return VideoDetailsDBManager().get_video_details(limit)


    def get_video_list(self):
        videos = VideoDetailsDBManager().get_video_all_details()
        video_list = []
        for video in videos:
            video_list.append(video.video_id)
        return video_list

    def search_video_with_title_or_description(self, title, description):
        filter = {}
        if title:
            filter["title__icontains"] = title
        if description:
            filter["description__icontains"] = description
        videos = VideoDetailsDBManager().get_video_all_details_filter(filter)
        return videos
