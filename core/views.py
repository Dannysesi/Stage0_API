from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
import pytz

class InfoAPIView(APIView):
    def get(self, request):
        data = {
            "email": "daniel.olusesi20@gmail.com",
            "datetime": datetime.now(pytz.UTC).isoformat(),
            "github_url": "https://github.com/Dannysesi/Stage0_API"
        }
        return Response(data)
