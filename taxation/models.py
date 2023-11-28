import uuid
from django.db import models
from custom_user.models import User
from django.core.validators import MinLengthValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class TaxPayer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
    name = models.CharField(
        blank=False,
        max_length=100,
        validators=[
            MinLengthValidator(5),
        ],
    )
    social_security_number = models.CharField(max_length=11, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    address = models.CharField(max_length=150, null=False, blank=False)
    phone_number = PhoneNumberField(
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.user.email


class Employment(models.Model):
    taxpayer = models.ForeignKey(TaxPayer, on_delete=models.CASCADE)
    employer_name = models.CharField(
        blank=False,
        max_length=100,
        null=False,
        validators=[
            MinLengthValidator(3),
        ],
    )
    income = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    taxes_withheld = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.taxpayer.user.email


class OtherIncome(models.Model):
    INCOME_CHOICES = [
        ("self_employment", "Self-Employment Income"),
        ("rental", "Rental Income"),
        ("interest", "Interest Income"),
        ("dividend", "Dividend Income"),
        ("capital_gains", "Capital Gains"),
        ("royalties", "Royalties"),
        ("alimony", "Alimony"),
        ("business", "Business Income"),
        ("unemployment_compensation", "Unemployment Compensation"),
        ("social_security", "Social Security Benefits"),
        ("pension", "Pension Income"),
        ("gambling_winnings", "Gambling Winnings"),
        ("prizes_awards", "Prizes and Awards"),
    ]

    taxpayer = models.ForeignKey(TaxPayer, on_delete=models.CASCADE)
    income_type = models.CharField(null=False, blank=False, choices=INCOME_CHOICES)
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.taxpayer.user.email


class Deduction(models.Model):
    DEDUCTION_CHOICES = [
        ("standard", "Standard Deduction"),
        ("itemized", "Itemized Deductions"),
        ("education", "Educational Expenses"),
        ("business", "Business Expenses"),
        ("hsa", "Health Savings Account (HSA) Contributions"),
        ("retirement", "Retirement Contributions"),
        ("job_related", "Job-Related Expenses"),
    ]

    taxpayer = models.ForeignKey(TaxPayer, on_delete=models.CASCADE)
    deduction_type = models.CharField(
        null=False, blank=False, choices=DEDUCTION_CHOICES
    )
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.taxpayer.user.email
