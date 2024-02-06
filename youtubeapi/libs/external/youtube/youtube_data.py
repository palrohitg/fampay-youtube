from youtubeapi.libs.constants import Constant
import requests
from youtubeapi.models import VideoDetail
from youtubeapi.utils import utils as utils
from youtubeapi.dbmanager.youtube import VideoDetailsDBManager


class YoutubeData:

    def __init__(self, query="cricket", max_results=10):
        self.search_api_url = Constant.Youtube.URL
        self.api_key = Constant.Youtube.API_KEY
        self.part = Constant.Youtube.PART
        self.query = query
        self.max_results = max_results

    def get_search_details(self, video_list):
        print("Start the request here as well")

        youtube_api_key = VideoDetailsDBManager().get_youtube_api_key()

        if youtube_api_key and youtube_api_key.key:
            query_params = {
                "key": youtube_api_key.key,
                "q": self.query,
                "maxResults": self.max_results,
                "part": self.part
            }
            try:
                response = requests.request("GET", self.search_api_url, params=query_params)
            except Exception as e:
                print(e)

            VideosList = []
            if response.status_code == 200:
                items = response.json().get('items')
                for item in items:
                    video_id = item.get("id").get("videoId")
                    title = item.get("snippet").get("title")
                    description = item.get("snippet").get("description")
                    published_at = utils.string_to_datetime(item.get("snippet").get("publishedAt"))
                    thumbnail_url = item.get("snippet").get("thumbnails").get("default").get("url")
                    video_obj = VideoDetail(video_id=video_id, title=title, description=description,
                                            published_at=published_at, thumbnail_url=thumbnail_url)
                    if video_id and video_id not in video_list:
                        VideosList.append(video_obj)
                return response.status_code, VideosList
            if response.status_code == 403:
                youtube_api_key.is_active = False
                youtube_api_key.save()
                self.get_search_details()

            return response.status_code, None
        else:
            print("All key are exhausted !!!")