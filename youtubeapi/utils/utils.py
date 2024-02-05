from django.utils import timezone
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


def get_current_datetime():
    return timezone.localtime(timezone.now())


def string_to_datetime(date_time_str):
    return datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%SZ")


def get_success_response(serialized_data=None):
    response_payload = {}
    if serialized_data is not None:
        response_payload["data"] = serialized_data

    response = Response(response_payload, status.HTTP_200_OK)
    return response
