from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timezone
from django.http import JsonResponse
from rest_framework import status
import pytz

def info_api(request):
    data = {
        "email": "daniel.olusesi20@gmail.com",
        "current_datetime": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "github_url": "https://github.com/Dannysesi/Stage0_API"
    }
    return JsonResponse(data, status=status.HTTP_200_OK)
