from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, TemplateView, View
from django_htmx.http import trigger_client_event
from django_tables2 import tables
from django_tables2.columns.templatecolumn import TemplateColumn

from carbonhomewatcher.forms import ApplianceForm
from carbonhomewatcher.models import Appliance, get_current_carbon_emissions


class ApplianceTable(tables.Table):
    toggle = TemplateColumn(template_name="appliance_toggle.html", orderable=False)

    class Meta:
        model = Appliance
        template_name = "django_tables2/bootstrap.html"
        exclude = ["id", "is_active"]
        orderable = False


class HomeView(TemplateView):
    template_name = "home.html"


class ApplianceTableView(TemplateView):
    template_name = "home.html#appliance-table"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appliance_table"] = ApplianceTable(Appliance.objects.order_by("name").all())
        return context


class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = "home.html#appliance-form"

    def form_valid(self, form):
        self.object = form.save()
        response = render(
            self.request,
            "home.html#appliance-created-alert",
            {"appliance": self.object},
        )
        return trigger_client_event(response, "newAppliance")


class CarbonEmissionsView(View):
    def get(self, request):
        return HttpResponse(f"{get_current_carbon_emissions()} gCO2eq/h")


def appliance_toggle_view(request, pk):
    appliance = get_object_or_404(Appliance, pk=pk)
    appliance.is_active = not appliance.is_active
    appliance.save()
