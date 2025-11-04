from django.db import models
from django.db.models import Sum

DEFAULT_CARBON_INTENSITY = 100  # gCO2eq/kWh


class Appliance(models.Model):
    name = models.CharField(max_length=100)
    power = models.FloatField()
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


def get_current_carbon_emissions() -> int:
    power_sum = Appliance.objects.filter(is_active=True).aggregate(Sum("power"))["power__sum"] or 0
    carbon_intensity = DEFAULT_CARBON_INTENSITY
    return round(carbon_intensity * power_sum)
