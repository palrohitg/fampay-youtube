from django.core.management.base import BaseCommand
from youtubeapi.libs.external.youtube.youtube_data import YoutubeData
from youtubeapi.controller.video_details_controller import VideoDetailController


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print("Backend JOB for Fetching Results")
        existing_video_details_list = self.get_exists_video()
        response_status, response_data = YoutubeData().get_search_details(
                                            existing_video_details_list
                                        )
        if response_data:
            VideoDetailController().create_video_details(response_data)


    def get_exists_video(self):
        return VideoDetailController().get_video_list()