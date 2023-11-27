from rest_framework.response import Response
from rest_framework import status
from uuid import uuid5, NAMESPACE_DNS
from random import getrandbits
from datetime import datetime


def response(data: dict, errors: dict = {}, code: int = status.HTTP_200_OK):
    return Response({"data": data, "errors": errors}, status=code)
