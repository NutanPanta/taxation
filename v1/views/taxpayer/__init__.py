from taxpayer.models import TaxPayer

from core.utilities import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from serializers.tax_docs import (
    CreateTaxPayerSerializer,
    ViewTaxPayerSerializer,
)


class TaxPayerAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        taxpayer = TaxPayer.objects.get(user=request.user.id)
        if taxpayer:
            taxpayer_with_related = TaxPayer.objects.prefetch_related(
                "employers", "other_incomes", "deductions"
            ).get(id=taxpayer.id)

            serializer = ViewTaxPayerSerializer(taxpayer_with_related)
            return response(serializer.data)
        return response(data={}, errors={})

    def post(self, request):
        serializer = CreateTaxPayerSerializer(
            data=request.data, context={"request": request}
        )

        _code = status.HTTP_400_BAD_REQUEST

        if serializer.is_valid():
            serializer.save()
            _code = status.HTTP_201_CREATED

        return response(
            data=serializer.data,
            errors=serializer.errors,
            code=_code,
        )

    def patch(self, request):
        taxpayer = TaxPayer.objects.get(user=request.user.id)

        if taxpayer:
            _code = status.HTTP_403_FORBIDDEN

            if taxpayer.reviewed:
                return response(
                    data={},
                    errors={
                        "detail": "Taxpayer record has already been reviewed and cannot be updated."
                    },
                    code=_code,
                )

            serializer = CreateTaxPayerSerializer(
                taxpayer, data=request.data, partial=True
            )

            _code = status.HTTP_400_BAD_REQUEST

            if serializer.is_valid():
                serializer.save()
                _code = status.HTTP_200_OK

            return response(data=serializer.data, errors=serializer.errors, code=_code)
        return response(data={}, errors={})
