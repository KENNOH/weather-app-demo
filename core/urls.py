from django.conf.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^location/(?P<city>.+?)/',views.WeatherComputeView.as_view(),name='weather_compute_metrics'),
]

