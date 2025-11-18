from django.urls import path

from carbonhomewatcher.views import ApplianceCreateView, HomeView, CarbonEmissionsView, CarbonIntensityView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('appliances/add', ApplianceCreateView.as_view(), name='appliance-create'),
    path('carbon-emissions/', CarbonEmissionsView.as_view(), name='carbon-emissions'),
    path('carbon-intensity/', CarbonIntensityView.as_view(), name='carbon-intensity'),
]
