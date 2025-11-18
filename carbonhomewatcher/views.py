from time import sleep

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape
from django.views import View
from django.views.generic import CreateView, TemplateView
from django_htmx.http import trigger_client_event

from carbonhomewatcher.forms import ApplianceForm
from carbonhomewatcher.models import Appliance
from carbonhomewatcher.services import carbon_emissions_service
from carbonhomewatcher.tables import ApplianceTable


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
    template_name = "home.html#appliance-form"

    def form_valid(self, form):
        self.object = form.save()
        context = {"appliance_table": get_appliance_table()}
        response = render(self.request, "home.html#appliance-table", context)
        return trigger_client_event(response, "applianceAdded")


class CarbonEmissionsView(View):
    def get(self, request):
        sleep(1)  # Simulate a delay in the response
        carbon_emissions = carbon_emissions_service.get_current_carbon_emissions()
        return HttpResponse(f"{escape(carbon_emissions)} gCO2eq/h")


class CarbonIntensityView(TemplateView):
    template_name = "home.html#carbon-intensity-alert"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carbon_intensity_dict = carbon_emissions_service.get_current_carbon_intensity_dict()
        context["carbon_intensity"] = carbon_intensity_dict.get("carbon_intensity")
        context["updated_at"] = carbon_intensity_dict.get("updated_at")
        context["zone"] = carbon_intensity_dict.get("zone")
        context["alert_level"] = carbon_intensity_dict.get("alert_level", "danger")
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return trigger_client_event(response, "carbonIntensityUpdated")
