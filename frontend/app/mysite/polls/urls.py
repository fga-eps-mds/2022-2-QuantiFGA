from django.urls import path

from .views import QuantiFGA


urlpatterns = [
    path("", QuantiFGA.as_view(), name="index"),
]
