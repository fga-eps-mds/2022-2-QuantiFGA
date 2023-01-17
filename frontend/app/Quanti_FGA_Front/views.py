from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.http.response import JsonResponse

from Quanti_FGA_Front.models import sala as Sala
from Quanti_FGA_Front.serializers import SalaSerializer

class salaApi(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    Sala_serializer = SalaSerializer
    serializer_class = SalaSerializer

