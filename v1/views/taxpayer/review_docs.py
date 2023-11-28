# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from taxpayer.models import TaxPayer
from serializers.tax_docs import CreateTaxPayerSerializer
from core.utilities import response


class TaxPayerReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        taxpayer = TaxPayer.objects.get(user=request.user)

        _code = status.HTTP_403_FORBIDDEN

        if taxpayer.reviewed:
            return response(
                data={},
                errors={},
                code=_code,
            )

        _code = status.HTTP_200_OK

        taxpayer.reviewed = True
        taxpayer.save()

        serializer = CreateTaxPayerSerializer(taxpayer)

        return Response(serializer.data, status=status.HTTP_200_OK)
