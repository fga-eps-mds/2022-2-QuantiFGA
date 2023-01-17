from django.conf.urls import url
from Quanti_FGA_Front import views

urlpatterns=[
    url(r'^sala$',views.salaApi),
    url(r'^sala$/([0-9]+)', views.salaApi)
]