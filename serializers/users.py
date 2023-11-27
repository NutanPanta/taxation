from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

        fields = (
            "email",
            "date_joined",
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
