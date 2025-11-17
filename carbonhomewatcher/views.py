from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from carbonhomewatcher.forms import ApplianceForm
from carbonhomewatcher.models import Appliance
from carbonhomewatcher.tables import ApplianceTable


class HomeView(TemplateView):
    template_name = "home.html"


def get_appliance_table():
    return ApplianceTable(Appliance.objects.all())


class ApplianceTableView(TemplateView):
    template_name = "partials/appliance_table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appliance_table"] = get_appliance_table()
        return context


class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = "home.html#appliance_form"

    def form_valid(self, form):
        self.object = form.save()
        context = {"appliance_table": get_appliance_table(), "appliance": self.object}
        return render(self.request, "partials/appliance_table.html", context)
