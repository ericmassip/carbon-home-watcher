from django.urls import path

from carbonhomewatcher.views import ApplianceCreateView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('appliances/add', ApplianceCreateView.as_view(), name='appliance-create'),
]
