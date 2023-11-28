# Generated by Django 4.2.7 on 2023-11-28 14:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxPayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)])),
                ('social_security_number', models.CharField(max_length=11)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=150)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('reviewed', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtherIncome',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('income_type', models.CharField(choices=[('self_employment', 'Self-Employment Income'), ('rental', 'Rental Income'), ('interest', 'Interest Income'), ('dividend', 'Dividend Income'), ('capital_gains', 'Capital Gains'), ('royalties', 'Royalties'), ('alimony', 'Alimony'), ('business', 'Business Income'), ('unemployment_compensation', 'Unemployment Compensation'), ('social_security', 'Social Security Benefits'), ('pension', 'Pension Income'), ('gambling_winnings', 'Gambling Winnings'), ('prizes_awards', 'Prizes and Awards')])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('taxpayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_incomes', to='taxpayer.taxpayer')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employer_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('income', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('taxes_withheld', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('taxpayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to='taxpayer.taxpayer')),
            ],
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('deduction_type', models.CharField(choices=[('standard', 'Standard Deduction'), ('itemized', 'Itemized Deductions'), ('education', 'Educational Expenses'), ('business', 'Business Expenses'), ('hsa', 'Health Savings Account (HSA) Contributions'), ('retirement', 'Retirement Contributions'), ('job_related', 'Job-Related Expenses')])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('taxpayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deductions', to='taxpayer.taxpayer')),
            ],
        ),
    ]
