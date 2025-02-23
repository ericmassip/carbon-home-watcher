from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django_htmx.http import trigger_client_event
from django_tables2 import tables

from carbonhomewatcher.forms import ApplianceForm
from carbonhomewatcher.models import Appliance


class ApplianceTable(tables.Table):
    class Meta:
        model = Appliance
        template_name = "django_tables2/bootstrap.html"
        exclude = ["id", "is_active"]
        orderable = False


class HomeView(TemplateView):
    template_name = "home.html"


class ApplianceTableView(TemplateView):
    template_name = "partials/appliance_table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table"] = ApplianceTable(Appliance.objects.order_by("name").all())
        return context


class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = "partials/appliance_form.html"

    def form_valid(self, form):
        self.object = form.save()
        response = render(
            self.request,
            "partials/appliance_created_alert.html",
            {"appliance": self.object},
        )
        return trigger_client_event(response, "newAppliance")
