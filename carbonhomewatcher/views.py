from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django_tables2 import tables

from carbonhomewatcher.forms import ApplianceForm
from carbonhomewatcher.models import Appliance


class ApplianceTable(tables.Table):
    class Meta:
        model = Appliance
        template_name = "django_tables2/bootstrap.html"
        exclude = ["id", "is_active"]
        orderable = False


def get_appliance_table():
    return ApplianceTable(Appliance.objects.all())


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appliance_table"] = get_appliance_table()
        return context


class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = "partials/appliance_form.html"

    def form_valid(self, form):
        self.object = form.save()
        context = {"table": get_appliance_table(), "appliance": self.object}
        return render(self.request, "partials/appliance_table.html", context)
