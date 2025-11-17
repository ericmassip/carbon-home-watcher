from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from carbonhomewatcher.forms import ApplianceForm
from carbonhomewatcher.models import Appliance
from carbonhomewatcher.tables import ApplianceTable


def get_appliance_table():
    return ApplianceTable(Appliance.objects.all())


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appliance_table"] = get_appliance_table()
        context["form"] = ApplianceForm()
        return context


class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    success_url = reverse_lazy("home")
