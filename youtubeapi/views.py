from rest_framework.views import APIView
from youtubeapi.serializer.video_details_serializer import VideoDetailSerializer
from youtubeapi.serializer.youtube_api_key_serializer import YoutubeAPIKeySerializer
from youtubeapi.serializer.search_serializer import  SearchSerializer
from youtubeapi.controller.video_details_controller import VideoDetailController
from youtubeapi.controller.youtube_api_key_controller import YoutubeAPIKeyController
from youtubeapi.utils import utils


# Create your views here.

class VideoDetailsView(APIView):
    serializer_class = VideoDetailSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        limit = serializer.validated_data.get('limit', 10)
        video_data = VideoDetailController().get_video_details_desc(limit)
        serialized_data = self.serializer_class(video_data, many=True).data
        return utils.get_success_response(serialized_data)


class YoutubeAPIKey(APIView):
    serializer_class = YoutubeAPIKeySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        youtube_key_response = YoutubeAPIKeyController().create_api_key(request.data)
        serialized_data = self.serializer_class(youtube_key_response).data
        return utils.get_success_response(serialized_data)

class SearchVideo(APIView):
    serializer_class = SearchSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get("title")
        description = serializer.vlaid_data.get("description")
        search_response = VideoDetailController().search_video_with_title_or_description(title,description)
        serialized_data = self.serializer_class(search_response, many=True).data
        return utils.get_success_response(serialized_data)