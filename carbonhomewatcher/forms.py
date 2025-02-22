from django import forms

from carbonhomewatcher.models import Appliance


class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = ["name", "power",]
        labels = {
            "power": "Power (kW)",
        }
