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

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.social_security_number = validated_data.get(
            "social_security_number", instance.social_security_number
        )
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.address = validated_data.get("address", instance.address)
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )

        self.update_nested_fields(
            instance.employers, validated_data.get("employers", []), Employment.objects
        )
        self.update_nested_fields(
            instance.other_incomes,
            validated_data.get("other_incomes", []),
            OtherIncome.objects,
        )
        self.update_nested_fields(
            instance.deductions, validated_data.get("deductions", []), Deduction.objects
        )

        instance.save()

        return instance

    def update_nested_fields(self, instance_list, validated_data_list, model_manager):
        for i, validated_data in enumerate(validated_data_list):
            if i < instance_list.all().count():
                instance = instance_list.all()[i]
                for key, value in validated_data.items():
                    setattr(instance, key, value)
                instance.save()
            else:
                model_manager.create(taxpayer=instance.taxpayer, **validated_data)


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
            "reviewed",
            "accepted",
        ]
