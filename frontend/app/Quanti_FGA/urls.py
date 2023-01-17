from django.contrib import admin
from django.urls import path, include
from Quanti_FGA_Front.views import salaApi
from rest_framework import routers as r

router = r.DefaultRouter()
router.register(r'salas',salaApi)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
