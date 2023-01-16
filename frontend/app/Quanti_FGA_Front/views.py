from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Quanti_FGA_Front.models import sala as Sala
from Quanti_FGA_Front.serializers import SalaSerializer


@csrf_exempt
def salaApi(request,id=0):
    if request.method=='GET':
        sala = Sala.objects.all()
        sala_serializer = SalaSerializer(sala, many=True)
        return JsonResponse(sala_serializer.data,safe=False)
    elif request.method=='POST':
        sala_data=JSONParser().parse(request)
        sala_serializer=SalaSerializer(sala=sala_data)
        if sala_serializer.is_valid():
            sala_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
    #elif request.method=='PUT':


