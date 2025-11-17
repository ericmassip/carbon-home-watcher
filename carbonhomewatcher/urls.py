from django.urls import path

from carbonhomewatcher.views import ApplianceCreateView, HomeView, ApplianceTableView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('appliances/add', ApplianceCreateView.as_view(), name='appliance-create'),
    path('appliances/table', ApplianceTableView.as_view(), name='appliance-table'),
]
