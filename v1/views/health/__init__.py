from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class HealthCheck(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return Response({"stauts": "If You See This The Server Is Healthy"})
