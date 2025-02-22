from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from django_htmx.http import HttpResponseClientRedirect
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appliance_table"] = ApplianceTable(Appliance.objects.order_by("name").all())
        return context


class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = "partials/appliance_form.html"

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseClientRedirect(redirect_to=reverse("home"))
