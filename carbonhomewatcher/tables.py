from django_tables2 import tables

from carbonhomewatcher.models import Appliance


class ApplianceTable(tables.Table):
    class Meta:
        model = Appliance
        template_name = "django_tables2/bootstrap.html"
        exclude = ["id", "is_active"]
        orderable = False
