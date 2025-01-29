from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.http import JsonResponse
import pytz

def info_api(request):
    data = {
        "email": "daniel.olusesi20@gmail.com",
        "datetime": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/Dannysesi/Stage0_API"
    }
    return JsonResponse(data)
