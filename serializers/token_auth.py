from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user=user)

        token["email"] = user.email
        token["date_joined"] = user.date_joined.strftime("%s")
        token["is_superuser"] = user.is_superuser
        token["is_staff"] = user.is_staff
        token["group"] = [i.name for i in user.groups.all()]

        return token
