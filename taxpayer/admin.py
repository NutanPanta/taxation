from v1.admin import admin_site
from taxpayer.models import TaxPayer, Employment, OtherIncome, Deduction

# Register your models here.
admin_site.register(TaxPayer)
admin_site.register(Employment)
admin_site.register(OtherIncome)
admin_site.register(Deduction)
