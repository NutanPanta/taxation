from rest_framework import serializers
from taxpayer.models import TaxPayer, Employment, OtherIncome, Deduction

from custom_user.models import User


class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = ["employer_name", "income", "taxes_withheld"]


class OtherIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherIncome
        fields = ["income_type", "amount"]


class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction
        fields = ["deduction_type", "amount"]


class CreateTaxPayerSerializer(serializers.ModelSerializer):
    employers = EmploymentSerializer(many=True)
    other_incomes = OtherIncomeSerializer(many=True)
    deductions = DeductionSerializer(many=True)

    class Meta:
        model = TaxPayer
        fields = [
            "name",
            "social_security_number",
            "date_of_birth",
            "address",
            "phone_number",
            "employers",
            "other_incomes",
            "deductions",
        ]

    def create(self, validated_data):
        employers_data = validated_data.pop("employers")
        other_incomes_data = validated_data.pop("other_incomes")
        deductions_data = validated_data.pop("deductions")

        user_id = (
            self.context["request"].user.user_id
            if "request" in self.context
            and hasattr(self.context["request"].user, "user_id")
            else None
        )

        user_instance = User.objects.get(pk=user_id)

        validated_data["user"] = user_instance

        taxpayer = TaxPayer.objects.create(**validated_data)

        for employer_data in employers_data:
            Employment.objects.create(taxpayer=taxpayer, **employer_data)

        for other_income_data in other_incomes_data:
            OtherIncome.objects.create(taxpayer=taxpayer, **other_income_data)

        for deduction_data in deductions_data:
            Deduction.objects.create(taxpayer=taxpayer, **deduction_data)

        return taxpayer


class ViewTaxPayerSerializer(serializers.ModelSerializer):
    employers = EmploymentSerializer(many=True, read_only=True)
    other_incomes = OtherIncomeSerializer(many=True, read_only=True)
    deductions = DeductionSerializer(many=True, read_only=True)

    class Meta:
        model = TaxPayer
        fields = [
            "name",
            "social_security_number",
            "date_of_birth",
            "address",
            "phone_number",
            "employers",
            "other_incomes",
            "deductions",
        ]
