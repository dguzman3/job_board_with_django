from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Test api view
class TestView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello World'}
        return Response(content)
