from django.urls import path

from carbonhomewatcher.views import ApplianceCreateView, HomeView, ApplianceTableView, CarbonEmissionsView, \
    appliance_toggle_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('appliances/add', ApplianceCreateView.as_view(), name='appliance-create'),
    path('appliances/table', ApplianceTableView.as_view(), name='appliance-table'),
    path('appliances/<int:pk>/toggle', appliance_toggle_view, name='appliance-toggle'),
    path('carbon-emissions/', CarbonEmissionsView.as_view(), name='carbon-emissions'),
]
