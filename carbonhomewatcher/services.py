import logging
import random
from abc import abstractmethod, ABC
from datetime import datetime

import requests
from django.conf import settings
from django.db.models import Sum
from django.utils import timezone

from carbonhomewatcher.models import Appliance
from webappconf.settings import ELECTRICITY_MAPS_API_KEY

ELECTRICITY_MAPS_API_ENDPOINT = "https://api.electricitymaps.com/v3"

log = logging.getLogger(__name__)


class CarbonEmissionsService(ABC):
    def get_current_carbon_emissions(self) -> int:
        """
        Returns current carbon emissions in gCO2eq/h based on active appliances and real-time carbon intensity. If
        carbon intensity download fails or active appliances have a total power consumption of 0 kW, returns 0 gCO2eq/h.
        """
        carbon_intensity_dict = self.get_current_carbon_intensity_dict()
        carbon_intensity = carbon_intensity_dict.get("carbon_intensity", 0)
        power_sum = Appliance.objects.filter(is_active=True).aggregate(Sum("power"))["power__sum"] or 0
        return round(carbon_intensity * power_sum)

    @abstractmethod
    def get_current_carbon_intensity_dict(self) -> dict:
        """
        Returns carbon intensity data in the form of a dict. If data is unavailable, returns an empty dict.

        Returns:
            (dict):
                - carbon_intensity (int): The carbon intensity in gCO2eq/kWh.
                - zone (str): The geographical zone for which the carbon intensity is reported.
                - updated_at (datetime): The timestamp when the data was last updated, localised.
                - alert_level (str): Alert level based on carbon intensity ('success', 'warning', or 'danger').
        """
        pass

    def _get_alert_level(self, carbon_intensity: int) -> str:
        if carbon_intensity <= 100:
            return 'success'
        elif carbon_intensity <= 200:
            return 'warning'
        else:
            return 'danger'


class RandomCarbonEmissionsService(CarbonEmissionsService):
    def __init__(self):
        log.warning("ELECTRICITY_MAPS_API_KEY not available in the Django settings module. Using "
                    "RandomCarbonEmissionsService instead...")
        self.carbon_intensity = random.randint(0, 300)

    def get_current_carbon_intensity_dict(self) -> dict:
        carbon_intensity_dict = {
            "carbon_intensity": self.carbon_intensity,
            "updated_at": timezone.localtime(),
            "zone": "RandomLand",
            "alert_level": self._get_alert_level(self.carbon_intensity),
        }
        log.info(f"Randomly generated carbon intensity data={carbon_intensity_dict}")
        return carbon_intensity_dict


class ElectricityMapsCarbonEmissionsService(CarbonEmissionsService):
    def get_current_carbon_intensity_dict(self) -> dict:
        """Fetches real-time carbon intensity data from the ElectricityMaps API."""

        carbon_intensity_dict = {}
        try:
            carbon_intensity_json_response = requests.get(
                f"{ELECTRICITY_MAPS_API_ENDPOINT}/carbon-intensity/latest",
                params={"temporalGranularity": "5_minutes"},
                headers={"auth-token": ELECTRICITY_MAPS_API_KEY}
            ).json()
            log.info(f"ElectricityMaps response={carbon_intensity_json_response}")

            carbon_intensity_dict = {
                "carbon_intensity": carbon_intensity_json_response["carbonIntensity"],
                "zone": carbon_intensity_json_response["zone"],
                "updated_at": timezone.localtime(
                    datetime.fromisoformat(carbon_intensity_json_response["updatedAt"])
                ),
                "alert_level": self._get_alert_level(carbon_intensity_json_response["carbonIntensity"]),
            }

        except Exception as e:
            log.error(f"The request to the ElectricityMaps API failed. Error={e}.")

        return carbon_intensity_dict


carbon_emissions_service = (
    ElectricityMapsCarbonEmissionsService()
    if settings.ELECTRICITY_MAPS_API_KEY
    else RandomCarbonEmissionsService()
)
