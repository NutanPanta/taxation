from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.utilities import response
from serializers.users import UserInfoSerializer


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserInfoSerializer(self.request.user, many=False)
        return response(data=serializer.data)
