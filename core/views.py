from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
import pytz

class InfoAPIView(APIView):
    def get(self, request):
        data = {
            "email": "your_registered_email@example.com",  # Replace this
            "datetime": datetime.now(pytz.UTC).isoformat(),
            "github_url": "https://github.com/yourusername/stage0-api"
        }
        return Response(data)
