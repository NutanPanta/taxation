from rest_framework_simplejwt.views import TokenObtainPairView
from serializers.token_auth import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
