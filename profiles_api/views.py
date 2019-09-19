from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Return a list of API features"""
        an_apiview = [
            'Uses HTTP methods as function (get, put, post, patch, delete)',
        ]

        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        })