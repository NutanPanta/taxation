from django.contrib.admin import AdminSite


class Taxation(AdminSite):
    site_header = "Taxation Project Management"
    site_title = "Taxation"
    index_title = "Admin Dashboard"


admin_site = Taxation(name="Taxation Admin")
