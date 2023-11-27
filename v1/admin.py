from django.contrib.admin import AdminSite


class WordCouch(AdminSite):
    site_header = "Word Couch Project Management"
    site_title = "Word Couch"
    index_title = "Admin Dashboard"


admin_site = WordCouch(name="Word Couch Admin")


