from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from core.utilities import response
from rest_framework import status
from rest_framework.permissions import AllowAny
from serializers.users import CreateUserSerializer


class UserCreateView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def post(self, request):
        serializer = CreateUserSerializer(data=self.request.data, many=False)

        _code = status.HTTP_400_BAD_REQUEST

        if serializer.is_valid():
            serializer.save()
            _code = status.HTTP_201_CREATED

        new_data = serializer.data.copy()

        if new_data.get("password", None):
            new_data.pop("password")

        return response(
            data=new_data,
            errors=serializer.errors,
            code=_code,
        )
